from random import randint


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0, 'No args'
    # Необходимо реализовать генератор 
    if len(args) == 1:			
    	for el in items:
    		if el[args[0]]:
    			yield el[args[0]]
    else:
    	for el in items:
	    	dct = {}
	    	for arg in args:
	    		if el[arg]:
	    			dct[arg] = el[arg]
	    	if dct:
	    		yield dct

# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    pass
    # Необходимо реализовать генератор
    for i in range(num_count):
    	yield randint(begin, end)
