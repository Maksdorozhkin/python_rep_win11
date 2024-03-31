# функция удаляет все гласные кроме y
def disemvowel(string_):
    remove_vowel = 'aeiouAEIOU'
    result = ''
    for i in string_:
        if i not in remove_vowel:
            result += i
    return result


print(disemvowel("This website is for losers LOL"))
