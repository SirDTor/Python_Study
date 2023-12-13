result = []


def invert_number(num):
    global result
    while num > 0:
        result.append(num % 10)
        num //= 10


number = 123456789
print(number)
invert_number(number)
print(result)
