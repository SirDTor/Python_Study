number = int(input('x = '))
result = ("Fizz Buzz" if number % 3 == 0 and number % 5 == 0 else
          "Fizz" if number % 3 == 0 else
          "Buzz" if number % 5 == 0 else
          str(number))
print(result)
