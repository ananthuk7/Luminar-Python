class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


f = open("student", "r")
for i in f:
    var=i.rstrip('\n').split(",")
    name=var[0]
    age=var[1]
    ob=Student(name,age)


