my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in my_list:
    print(i**2)

# открываем текстовый файл
file = open(
    "C:\\Users\\md\\Documents\\python\\cycle_iterator_generator\\sample.txt", "r")

for x in file.readlines():
    print(x)

# после открытия файла его необходимо закрыть file.close()
file.close()

# чтобы не закрывать вручную файл можно его открыть внутри контекстного оператора
with open(
        "C:\\Users\\md\\Documents\\python\\cycle_iterator_generator\\sample.txt", "r") as file:
    for x in file.readlines():  # перебирает построчно
        print(x)
