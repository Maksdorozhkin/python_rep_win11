# Вычисляем факториал рекурсией
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(5))

# Суммирование чисел от 1 до n


def summation(n):
    if n == 1:
        return 1
    return summation(n - 1) + n


print(summation(10))

# Сумма нечетных чисел
# элементарное решение


def sum_odd(list):
    if not list:
        return 0
    if list[0] % 2 != 0:
        # берем первое значение списка и если оно нечетное то применяем рекурсию только уже второе значение
        return list[0] + sum_odd(list[1:])
    else:
        return sum_odd(list[1:])


print(sum_odd([1, 1, 1, 2, 2, 2]))

print('')


def sum_even(list):
    if not list:
        return 0
    if not list[0] % 2 != 0:
        # берем первое значение списка и если оно нечетное то применяем рекурсию только уже второе значение
        return list[0] + sum_even(list[1:])
    else:
        return sum_even(list[1:])


print(sum_even([1, 1, 1, 2, 2, 2]))


# Сумма нечетных чисел и вычитание четных


def sum_sub(list):
    if not list:
        return 0
    if list[0] % 2 != 0:
        return list[0] + sum_sub(list[1:])
    else:
        return -list[0] + sum_sub(list[1:])


print(sum_sub([1, 1, 1, 1, 2, 2, 2, 2,]))
