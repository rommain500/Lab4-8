from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import date
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("")
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html',args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("")

def reg(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return HttpResponseRedirect("")
        else:
            args['form']=newuser_form
    return render_to_response('reg.html',args)


