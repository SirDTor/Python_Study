from collections import OrderedDict
import re


chars_popularity = {}
words_popularity = {}


def FindPopularChars(origtext: str):
    dataChars = OrderedDict()
    for char in origtext:
        if char != ' ':
            if dataChars.__contains__(char):
                dataChars[char] += 1
            else:
                dataChars[char] = 1
            countChar = dataChars[char]
            chars_popularity[char] = countChar


def FindPopularWords(origtext: str):
    dataWords = OrderedDict()
    arrayOfWord = re.split(", | ", origtext)
    for word in arrayOfWord:
        if dataWords.__contains__(word):
            dataWords[word] += 1
        else:
            dataWords[word] = 1
        countWords = dataWords[word]
        words_popularity[word] = countWords


text = "hello, word of word"
FindPopularChars(text)
FindPopularWords(text)
print(chars_popularity)
print(words_popularity)
