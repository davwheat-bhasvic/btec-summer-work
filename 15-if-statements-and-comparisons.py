def max_num(n1, n2, n3):
    # 2x less comparisons than FCC's version
    max1 = n1 if n1 >= n2 else n2
    return n3 if n3 >= max1 else max1


print(max_num(10, 20, 30))
print(max_num(10, 30, 20))
print(max_num(30, 20, 10))
