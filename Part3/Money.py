while True:
    try:
        rawValue = float(input("Enter the value to convert to money: "))
        if rawValue > 0:
            rawValue = round(rawValue, 2)
            formattedValue = "{:,.2f}".format(rawValue)
            print(formattedValue)
            break
        else:
            print("Number must be more then {rawValue}, try again".format(
                rawValue=rawValue))
    except ValueError:
        print('Value must be a number')
