number = int(input('number = '))
if number % 2 != 0:
    print("Плохо")
elif (number >= 2 and number <= 5) and number % 2 == 0:
    print("Неплохо")
elif (number >= 6 and number <= 20) and number % 2 == 0:
    print("Так себе")
elif number > 20 and number % 2 == 0:
    print("Отлично")
