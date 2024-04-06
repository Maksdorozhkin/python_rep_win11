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

# рекурсия функция возвращает саму себя


def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))

# более простой способ


def flattens(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flattens(item)
        else:
            yield item


print(list(flattens(lol)))
