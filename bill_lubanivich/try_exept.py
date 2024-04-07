# Размещаем код в блоке try и используйте блок except
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print("Need a position between 0 and", len(
        short_list)-1, ' but got', position)

# создаем собственное исключение


class UppercaseException(Exception):
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
