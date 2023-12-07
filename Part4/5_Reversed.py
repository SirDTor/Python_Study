from random import randint
try:
    n1 = input("Исходное число: ")
    n1 = str(n1)
    n2 = n1[::-1]
    n2 = str(n2)
    if int(n2) > 2**31 - 1 or int(n2) < -2**31:
        n2 = 0
    print('Обратное число:', str(n2))
except Exception:
    print('Значение должно быть числом.')
