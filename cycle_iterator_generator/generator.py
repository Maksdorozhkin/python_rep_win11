def file_lines_generator(filename):
    with open(filename, "r") as file:
        while line := file.readline():
            yield line  # yield превращает функцию в генератор, суть идеи в том что файл читается построчно после каждой строчки функция переводит каретку на следующую строку и становится на паузу и так строка за строкой т.е не хранит весь файл в памяти, это хорошо подходит для экономии ресурсов


for lines in file_lines_generator("C:\\Users\\md\\Documents\\python\\cycle_iterator_generator\\sample.txt"):
    print(lines)
