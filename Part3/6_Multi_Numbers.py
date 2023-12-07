result = 1
try:
    inputNumber = str(input("Enter the number: "))
    for number in inputNumber:
        if number != '0':
            result *= int(number)
            print(result)
    print(result)
except ValueError:
    print('Value must be a number')
