# 9.1

def good(a):
    return a


print(good(['Harry', 'Ron', 'Hermione']))

# 9.2


def get_ops():
    my_list = []
    for i in range(10):
        if i % 2 == 1:
            my_list += str(i)
    return my_list[2]


print(get_ops())


# 9.3
# декоратор
def test(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Start"
    return new_function

# функция


@test  # вызов декоратора
def end():
    pass


print(end())

# 9.4


class OopsException(Exception):
    pass


def m_f(a):
    return a[3]


raise OopsException('Caught an oops')
