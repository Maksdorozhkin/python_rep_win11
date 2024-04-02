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

i = 20
while i >= 1:
    print(i)
    i = (i - 1)


# проверяет бесконечно введенный пароль
inp = input("password: ")
password = 'rdf34dsg'
while inp != password:
    print("Неправильный пароль!: ")
    inp = input("password: ")
