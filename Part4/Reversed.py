from random import randint

n1 = randint(123, 987)
print("Исходное число:", n1)
n1 = str(n1)

n2 = n1[::-1]
n2 = str(n2)
print('Обратное число:', n2)
