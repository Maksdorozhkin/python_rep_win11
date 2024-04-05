# создаем словарь с помощью функции zip
english = 'dog', 'cat', 'walrus'
french = 'chien', 'chat', 'morse'
new_dict = zip(english, french)
print(type(new_dict))
new_dict = dict(new_dict)
print(type(new_dict))

new_dict['new_key'] = 10
print(new_dict)

# получаем значение ключа с помощью get

print(new_dict.get('new_key'))
print(new_dict.get('one_key', 'Нет такого ключа!'))

print('new_key' in new_dict)
# get all key
print(new_dict.keys())
print(list(new_dict.keys()))

# получаем значения ключей
print(list(new_dict.values()))

# получаем ключ значение
print(list(new_dict.items()))

# объединяем словари с помощью **a **b
first_dict = {'a': 'agony', 'b': 'bliss'}
print({**new_dict, **first_dict})

# update() копирует ключи и значение из одного словаря в другой

# удаляем элементы
del first_dict['a']
print(first_dict)
print(first_dict.pop('b'))
print(first_dict)

# удалить все из словаря clear()

# copy()

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
original_signals = signals.copy()
print(original_signals)

#
signals['blue'] = 'confuse everyone'
print(signals)

# deepcopy() - глубокое копирование
# итерация по словарям по ключам
for i in signals.keys():
    print(i)

# по значениям
for i in signals.values():
    print(i)
print('')
# ключ значение
for i in signals.items():
    print(i)

# включения словарей (проходим по строке циклом и считаем сколько раз буква встречается в строке)
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts2 = {letter2: word.count(letter2) for letter2 in set(word)}
print(letter_counts2)

print(letter_counts == letter_counts2)


#!!!!!!!!!!!!!!!!!!!!!!!!!!
# условные проверки if и более одного бола for
# в данном примере проверяем сколько раз буквы из 1 переменной включаются во второй
x1 = 'aeiou'
x2 = 'onomatopoeia'
vowel_counts = {letter: x2.count(letter)
                for letter in set(x1) if letter in x2}
print(vowel_counts)
