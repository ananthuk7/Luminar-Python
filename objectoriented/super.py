class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printVal(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, roll_no, mark, name, age):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.mark = mark

    def pri(self):
        print(self.roll_no, self.mark)


cr = Student(2, 34, "anu",22)
cr.printVal()
cr.pri()
