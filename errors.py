"""try:
    number = int(input("Enter a non-zero integer: "))
    print("10 / {} = {}".format(number, 10.0/number))
except ValueError:
    print("You did not enter an integer.")
except ZeroDivisionError:
    print("You cannot enter 0")


"""

while True:
    try:
        number = int(input("Enter an integer: "))
        print("Your integer number is", number, "\nThank You! GoodBye!")
        break
    except ValueError:
        print("Try again")