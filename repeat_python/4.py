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

# 4.4
