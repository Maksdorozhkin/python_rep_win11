# задача необходимо создать функцию которая будет делать каждое слово с большой буквы 1 вариант неправильный
def to_jaden_case(string):
    res_str = ""
    res_list = []
    b = string.split(" ")
    for i in b:
        res_list.append(i.capitalize())
    for z in res_list:
        res_str += z
        res_str += " "
    return res_str


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


def asd(string):
    return ' '.join(word.capitalize() for word in string.split())


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if not number % 2 == 1:
        return 'Even'
    else:
        return "Odd"


even_or_odd(3)


# найти наименьшее число в массиве
def find_smallest_int(arr):
    a = arr[:]
    return min(a)


print(find_smallest_int([78, 56, 232, 12, 11, 43]))

# выяснить является ли число фактором другого числа


def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False


def check_for_factor(base, factor):
    return base % factor == 0
