from word2number import w2n
text = "start 5 one two tree 7 end"
array = text.split(' ')
num_of_word = 0
for word in array:
    try:
        for i in range(1000):
            if type(w2n.word_to_num(word)) == int:
                continue
    except:
        num_of_word += 1
if num_of_word == 3:
    print('True')
else:
    print('False')
