from collections import OrderedDict
import re


chars_popularity = {}
words_popularity = {}


def findpopularchars(origtext: str):
    datachars = OrderedDict()
    for char in origtext:
        if char != ' ' and char !=',':
            if datachars.__contains__(char):
                datachars[char] += 1
            else:
                datachars[char] = 1
            countchar = datachars[char]
            chars_popularity[char] = countchar


def findpopularwords(origtext: str):
    datawords = OrderedDict()
    arraypofword = re.split(", | ", origtext)
    for word in arraypofword:
        if datawords.__contains__(word):
            datawords[word] += 1
        else:
            datawords[word] = 1
        countwords = datawords[word]
        words_popularity[word] = countwords


text = "hello, word of word"
findpopularchars(text)
findpopularwords(text)
print(chars_popularity)
print(words_popularity)
