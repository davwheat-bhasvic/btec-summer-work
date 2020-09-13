class Student:
    def __init__(self, name, age, is_excluded, avg_gcse_grade):
        self.name = name
        self.age = age
        self.is_excluded = is_excluded
        self.avg_gcse_grade = avg_gcse_grade

    def isOxbridge(self):
        return self.avg_gcse_grade >= 8


student1 = Student("David Wheatley", 16, False, 9)
naughtyStudent = Student("James Boyer", 17, True, 5)

print(student1.isOxbridge())
print(naughtyStudent.isOxbridge())
