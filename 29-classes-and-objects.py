class Student:
    def __init__(self, name, age, is_excluded):
        self.name = name
        self.age = age
        self.is_excluded = is_excluded


student1 = Student("David Wheatley", 16, False)
naughtyStudent = Student("James Boyer", 17, True)

print(student1.name)
print(naughtyStudent.age)
