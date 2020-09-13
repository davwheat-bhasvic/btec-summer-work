num = input("Enter a number: ")

try:
    num = int(num)
except ValueError:
    print("Input wasn't a valid number")
    exit()

print(num, "x 5 =", num * 5)

print("\n-----------------------------\n")

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name, "\nage:", age)
