word = input('Введите слово: ')
ispalindrom = False


def palindrom_check(check_word):
    if word == word[::-1]:
        ispalindrom = True
    return ispalindrom


ispalindrom = palindrom_check(word)
print(word, 'Палиндром?', ispalindrom)
