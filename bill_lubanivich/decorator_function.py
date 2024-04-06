# функция декоратор

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running Function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

# напишем еще один декоратор


def square_int(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return new_function

# функция


def add_ints(a, b):
    return a + b


cooler_add_ints = document_it(add_ints)  # создание декоратора вручную
cooler_add_ints(3, 5)


# более удобный вариант применения декоратора

@document_it  # применение декоратора
@square_int  # применение второго
def min_int(a, b):
    return a - b


min_int(10, 5)
