my_dict = {'Andrey': 1981, 'Ksuhsa': 2017}
print(my_dict)
print(my_dict['Andrey']) # Выведите на экран одно значение по существующему ключу
my_dict['Anton'] = 2020 # одно по отсутствующему из словаря, он автоматически добавит в словарь

my_dict.update({'Vova': 2019, 'Misha': 1987})
print(my_dict)
a = my_dict.pop('Vova')
print(a)
print(my_dict)
my_set = {1, 2, 3, 5, 6, 18, 18, 1, 2, 3, 4, 5, 'string', 'aplle', (1, 2, 3)} # множество хранит уникальные значения
print(my_set)

my_set.update([88, 99]) #Метод add() добавляет во множество один объект,Метод update() позволяет добавить сразу несколько элементов в скобках[]
print(my_set.discard(6))
print(my_set)
#print(my_set.discard(2))
#book = my_dict.pop('Vova')
#print(my_dict)
#del my_dict['Misha'] удалить
#print(my_dict.get('Misha'))
#print(my_dict)
