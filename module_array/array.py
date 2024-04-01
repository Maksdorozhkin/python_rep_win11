# модуль array (массивы - это типа списков но элементы одного типа)
from array import array

my_int_array = array('i', [4, 5, 10, 5, 7, 5])
print(my_int_array)
print(type(my_int_array))

my_int_array.append(15)

print(my_int_array)

print(my_int_array.count(5))
my_int_array.pop()

print(my_int_array)

print(len(my_int_array))

# итерация
for elem in my_int_array:
    print(elem)

print(my_int_array[-1])


# сохраняем массив в файле и потом прочтем его из файла
with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)


imported_array = array('i')

# чтение массива из файла
with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)
