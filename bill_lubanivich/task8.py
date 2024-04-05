# 8.1
english = 'dog', 'cat', 'walrus'
french = 'chien', 'chat', 'morse'
e2f = dict(zip(english, french))
print(e2f)
# 8.2
print(e2f['walrus'])
# 8.3 поменять местами ключи и значения в словаре
f2e = {v: k for k, v in e2f.items()}
print(f2e)
# 8.4
print(f2e['chien'])
# 8.5
print(set(e2f))
# 8.6
life = {
    'animals': {'cats': {}, 'octopi': {}, 'emus': {}},
    'plants': {},
    'other': {},
}
# 8.7
print(life.keys())
# 8.8
print(life['animals'].keys())
# 8.9
print(life['animals']['cats'])
# 8.10
squares = {x: x**2 for x in range(10)}  # создаем словарь с помощью генератора
print(squares)
# 8.11
odd = set(x for x in range(10) if x % 2 == 1)
print(odd)
print(type(odd))
# 8.12
for item in ('got' + str(num) for num in range(10)):
    print(item)
# 8.13
key = ('optimist', 'pessimist', 'troll')
values = ('the glass is half full', 'the glass is half empty',
          'how did you get a glass')
dict_k_v = dict(zip(key, values))
print(dict_k_v)
# 8.14
print('')
titles = ['Creature of habit', 'crewel fate', 'sharks of the plane']
plots = ["a nam turns into a monster",
         'a haunted yarn shop', 'check your exits']
res = dict(zip(titles, plots))
print(res)
