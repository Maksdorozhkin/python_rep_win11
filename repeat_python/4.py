# while

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b


# if elif else
# x = input(input("Введи число: "))
x = 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zeroo')
elif x == 1:
    print('Single')
else:
    print('More')

# for
words = ['anal', 'big tits', 'hardcore']
for i in words:
    print(i, len(i))

# Strategy: iterate over a copy
users = {'Hans': 'active', 'Eleonore': 'inactive'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# Создание новой коллекции
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)


# range

for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# перебор индексов последовательности

a = ['big tits', 'big ass', 'hot minet']
for i in range(len(a)):
    print(i, a[i])

print(range(10))

print(sum(range(10)))

# 4.4 break continue
# стратегия разделения на простые числа
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# стратегия разделения на четные и нечетные
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# 4.6 match


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I`m a teapot"
        case 401 | 403:
            raise ValueError("Not a point")


print(http_error(418))

#
point = (0, 20)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            raise ValueError("Not a point")


my_point = Point(0, 0)
where_is(my_point)
