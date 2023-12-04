firstName = input("Enter your name")
lastName = input("Enter you surname")
if firstName == '' and lastName == '':
    print("Null expression")
else:
    print("Hello {firstName} {lastName}! You just delved into Python. Great start!".format(
        firstName=firstName, lastName=lastName))
