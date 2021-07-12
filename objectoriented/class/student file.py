class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


f = open("student", "r")
for i in f:
    i.rstrip('\n').split(" ")
    name=i[0]
    age=i[1]

