from random import randint
num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
print('Первое число = {num1}\nВторое число = {num2}\nТретье число = {num3}\nРезультат = '
      .format(num1=num1, num2=num2, num3=num3),
      round(((num1+num2+num3)/3), 2))
