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
