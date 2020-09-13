with open("26-employees.txt", "r") as x:
    for line in x.readlines():
        print(line.rstrip("\n"))
