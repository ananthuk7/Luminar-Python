class Company:
    def employee(self, name, eid, salary, cname):
        self.name = name
        self.eid = eid
        self.salary = salary
        self.cname = cname

    def printEmployee(self):
        print("eid : ", self.eid, "name :", self.name, "salary: ", self.salary, "company name: ", self.cname)

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


em1 = Company()
em1.employee("ananthu", 100, 100000, "AOTI")
em1.printEmployee()
em1.employee("ananth", 10, 10000, "AOT")
em1.printEmployee()

# num=Company()
# num.add(5,6)
# print("sum is",num.num1+num.num2)


class Student:
    def stud(self, name, rollno, mark, school):
        self.name = name
        self.rollno = rollno
        self.mark = mark
        self.school = school
        print("name " " rollno " " mark " " school")
        print(name, " ", rollno, " ", mark, "   ", school)


s1 = Student()
s1.stud(input("enter the name"), int(input("enter the rollnumber")), int(input("enter the mark")), input("school name"))
