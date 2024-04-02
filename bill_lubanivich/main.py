# оператор присваивания (морж) :=

# tweet_limit = 280
# tweet_string = "Blah" * 50
# dif = tweet_limit - len(tweet_string)
# if dif >= 0:
#     print("Bla bla bla")


# # то же самое но с оператором присваивания

# tweet_limit = 280
# tweet_string = "Blah" * 50
# if dif := tweet_limit - len(tweet_string) >= 0:
#     print("Bla bla bla")

# # while

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# # break
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())


# continue
# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q':  # выход
#         break
#     number = int(value)
#     if not number % 2 == 0:  # нечетное число пропускаем
#         continue
#     print(number, "squared is", number*number)

# прерываем цикл while с помощью else

# numbers = [1, 2, 3, 5]
# position = 0
# # Начинает цикл while, который продолжается, пока position меньше длины списка numbers
# while position < len(numbers):
#     # Получает значение на текущей позиции в списке numbers и присваивает его переменной number.
#     number = numbers[position]
#     if number % 2 == 0:  # четное
#         print('Found even number', number)
#         break
#     position += 1
# # Если цикл while завершается без встречи оператора break (т.е. ни одно чётное число не было найдено), выполняется этот блок else.
# else:
#     print("No even number found")


# другой пример цикла while
# i = 1
# n = int(input("Введи число: "))
# while i <= n:
#     print('Hello')
#     i = i+1

# выводим числа в порядке убывания

# i = 20
# while i >= 1:
#     print(i)
#     i = (i - 1)


# проверяет бесконечно введенный пароль
# inp = input("password: ")
# password = 'rdf34dsg'
# count = 0
# while inp != password:
#     count += 1
#     print("Неправильный пароль!: ")
#     inp = input("password: ")
# print("Вы потратили", count, "попыток!")


# удаляем все 3 из списка
# a = [1, 2, 3, 4, 5] * 5
# print(a)

# while 4 in a:
#     a.remove(4)
#     print(a)

# пример со строками используем срезы строк и цикл while
# s = 'privet1~'
# while len(s) > 0:
#     print(s[0], s[1:])
#     s = s[1:]

# while len(s) > 0:
#     # print(s[0],)
#     bukva = s[0]
#     if bukva >= 'a' and bukva <= 'z':
#         print(bukva, "small")
#     elif bukva >= 'A' and bukva <= 'Z':
#         print(bukva, "Big")
#     elif bukva.isdigit():
#         print(bukva, "Цифра")
#     else:
#         print(bukva, "Знак")
#     s = s[1:]

# цикл for
# word = 'thud'
# for letter in word:
#     print(letter)

# break

# for letter in word:
#     if letter == 'u':
#         break
#     print(letter)
# continue пропускает итерации

# else
# for letter in word:
#     if letter == 'x':
#         print("Eek! An 'x'!")
#         break
#     print(letter)
# else:
#     print("No 'x' in there.")

# генерируем числовые последовательности с помощью функции range()
for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)

print(list(range(2, -1, -1)))
print(list(range(0, 11, 2)))


print(list(range(3, -1, -1)))

# задача 6.2 не понял условие
# guess_me = 7
# number = 1
# start = int(input("Введи число: "))
# while start < guess_me:
#     print("Too low")
#     number = number + 1
#     if start == guess_me:
#         print("found it")
#         break
#     if number > guess_me:
#         print("oops")
#         number += 1
#         break
