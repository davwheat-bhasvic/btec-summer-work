try:
    answer = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

try:
    number = int(print("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
