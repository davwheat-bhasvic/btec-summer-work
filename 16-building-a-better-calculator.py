num1 = float(input("Enter 1st number: "))
op = input("Enter operator:   ")
num2 = float(input("Enter 2nd number: "))

if op == "+":
    val = num1 + num2
elif op == "-":
    val = num1 - num2
elif op == "*" or op == "x":
    val = num1 * num2
elif op == "/":
    val = num1 / num2

print(val)
