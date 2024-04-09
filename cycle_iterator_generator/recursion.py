my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': {
        'a': 1,
        'b': {'a': 5,
              'b': {
                  'a': 3
              }}
    }
}

# for i in my_dict.values():
#     if isinstance(i, dict):
#         for j in i.values():
#             print(j)
#     else:
#         print(i)
# Для перебора словаря не известной глубины хорошо подходит рекурсивная функция, рекурсивная функция вызывает сама себя, допустим нам нужно получить одни значения словаря


def dict_traversal(d):
    for v in d.values():
        # если значение словарь то мы запускаем опять нашу функцию только со значением внутреннего словаря
        if isinstance(v, dict):
            dict_traversal(v)
        else:
            print(v)


dict_traversal(my_dict)
