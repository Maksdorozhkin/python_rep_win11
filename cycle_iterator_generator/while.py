i = 2
while i:
    print("Hello")
    i -= 1

with open(
        "C:\\Users\\md\\Documents\\python\\cycle_iterator_generator\\sample.txt", "r") as file:
    while line := file.readline():  # Оператор := называется моржом он позволяет сразу объявить переменную в данном случае line
        print(line)
