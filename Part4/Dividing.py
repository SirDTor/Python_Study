from random import randint
num1 = randint(0, 100)
num2 = randint(0, 100)

print('Первое число = {num1}\nВторое число = {num2}'
      .format(num1=num1, num2=num2), '\nЧисло = ', num1//num2, '\nОстаток = ', num1 % num2)
