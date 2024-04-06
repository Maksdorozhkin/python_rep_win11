def agree():
    return True


agree()
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')


# функция показывает является ли ее аргумент None True False
def whatis(thing):
    if thing is None:
        return None
    elif thing:
        return True
    else:
        return False


print(whatis(0.0001))

# ошибки с аргументами по умолчанию, ставить аргументом по умолчанию изменяемый объект в данном случае список


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')

# корректно


def works(arg):
    result = []
    result.append(arg)
    print(result)


works('a')
works('b')


# можно по другому решить проблему
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')
nonbuggy('b')

# аргумент *args пример использования


def print_more(req1, req2, *args):
    print('Need this one: ', req1)
    print('Need this one two: ', req2)
    print('All the rest: ', args)


print_more('cap', 'glovers', 'scarf', 'monocle', 'mustache wax')

# знак * в определении функции говорит о том что параметры нужно передавать как именованные аргументы, если мы хотим использовать их значения по умолчанию, пример функции которая работает как срез


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print_data(data, start=3, end=6)
# print_data(data, end=7)
print('')

# Изменяем изменяемы аргументы внутри функции
# добавляем строки документации в функцию
outside = ['one', 'fine', 'day']


def mangle(arg):
    '''в функцию можно добавить строки документации, например описание что она делает, в данном случае мы изменяем изменяемы аргументы внутри функции'''
    arg[1] = 'сиськи'
    print(outside)


print(outside)
mangle(arg=outside)
print(help(mangle))
print(mangle.__doc__)  # выдает документацию без форматирования
print('')

# передаем функцию в качестве аргумента к функции


def answer():
    print(42)


def run_something(func):
    func()


print(run_something(answer))


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_arg(func, arg1, arg2):
    func(arg1, arg2)


print(run_something_with_arg(add_args, 5, 5))

# лямбда функции


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return print(word.capitalize() + '!')


#
print(edit_story, enliven)

# передаем lambda функцию как аргумент функции
edit_story(stairs, lambda word: word.capitalize() + '!')

# функции генераторы (вместо return передается yield)
print('')


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


ranger = my_range(2, 200, 50)

for x in ranger:
    print(x)

print('')

# включения генераторов
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
for t in genobj:
    print(t)
