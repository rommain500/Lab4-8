# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
def print_result(printable_func):
	def decorated(*args):
		print(printable_func.__name__)
		if type(printable_func(*args)) == list:
			for i in printable_func(*args):
				print(i)
		elif type(printable_func(*args)) == dict:
			for key, val in printable_func(*args).items():
				print('{} = {}'.format(key, val))
		else:
			print(printable_func(*args))
	return decorated