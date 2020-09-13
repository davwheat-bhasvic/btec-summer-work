def pow(num, exponent):
    n = 1

    for _ in range(exponent):
        n *= num

    return n


print(pow(3, 2))
print(pow(3, 4))
print(pow(2, 3))
