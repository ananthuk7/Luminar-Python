class Person:
    def pdetails(self, name, age, adrs):
        self.name = name
        self.age = age
        self.adrs = adrs


class Student(Person):
    def sdetails(self, rollno, department, mark):
        self.rollno = rollno
        self.department = department
        self.mark = mark
st1=Student()
st1.pdetails("ananthu",23,"abc")
st1.sdetails(1,"cs",100)