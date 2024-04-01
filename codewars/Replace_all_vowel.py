# Задача поменять все гласные на !

def rep_all_vowel(st):
    vowels = "aeiouAEIOU"
    res = "".join(s if s not in vowels else "!" for s in st)
    return res


print(rep_all_vowel("Hi!"))
