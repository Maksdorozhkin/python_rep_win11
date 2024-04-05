empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8, }
print(type(even_numbers))
odd_numbers = {1, 3, 5, 7, 9}

# функция set() (отбрасывает все повторяющиеся)

print(set('letters'))

# при передачи словаря возвращает только ключи
# len() показывает длину множества
# функция add()
s = set((1, 2, 3))
print(s)

s.add(4)
print(s)
# удаляем элемент
s.remove(3)
print(s)

# for in
furniture = set(('sofa', 'ottoman', 'table'))
for i in furniture:
    print(i)

# проверяем на наличие с помощью оператора in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'vodka', 'kahlua'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
for name, y in drinks.items():
    if 'vodka' in y:
        print(name)

for name, x in drinks.items():
    if 'vodka' in x and not ('vermuth' in x or 'cream' in x):
        print(name)

# используем оператор пересечения множеств & (к примеру ищем напиток с вермутом или апельсиновым соком )

for name, z in drinks.items():
    if z & {'vermouth', 'orange juice'}:
        print(name)

print("")

for name, u in drinks.items():
    if 'vodka' in u and not u & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wrus = drinks['white russian']

print('')
# пересечение множеств & (intersection())

a = {1, 2}
b = {2, 3}
print(a & b)

print(bruss & wrus)
print('')

# объединение множеств используем оператор | или (union())

print(a | b)
print(bruss | wrus)
print("")

# разность множеств можно получить с помощью символа - или (difference()) (члены только первого множества но не второго)
print(a-b)
print(a.difference(b))
print(bruss - wrus)
print(wrus - bruss)
print('')

# ИЛИ для выполнения исключающего используйте оператор ^ или функцию (symmetric_difference())

print(a ^ b)
print(bruss ^ wrus)
print('')

# Проверить является ли одно множество подмножеством другого можно с помощью оператора <= или функции issubset()

print(a <= b)
print(bruss <= wrus)
print('')

# НАДМНОЖЕСТВО противоположно подмножеству для определения используется оператор >= или функция issuperset()

print(a >= b)
print(wrus >= bruss)
print("")

# Включение множеств
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# неизменяемое множество frozenset()
fs = frozenset([1, 2, 3, 4])
print(fs)
