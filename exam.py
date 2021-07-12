# class Vehicle:
#     def __init__(self,name,color,model):
#         self.name=name
#         self.color=color
#         self.model=model
# class Car(Vehicle):
#     def __init__(self,price):
#         super().__init__(name,color,model)
#         self.price=price
# # 2

# class College:
#     def printCollege(self):
#         print("college")
# class Student(College):
#     def printStudent(self):
#         print("student")
# class Teacher(Student,College):
#     def printTeacher(self):
#         print("Teacher")

# 3

# class Book:
#     def __int__(self,Library_name, book_name, author, pages):
#         self.Library_name=Library_name
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages

#5
# over-riding...same method name and same number of arguments
# child class override parent class method
#
# class Teacher:
#     def printVal(self,name):
#         self.name=name
#         print(self.name)
#
# class Student(Teacher):
#     def printVal(self,name):
#         self.name=name
#         print(self.name)


#6
#
# class Student:
#     def __init__(self,name,rollno,course,mark):
#         self.name=name
#         self.rollno=rollno
#         self.school=course
#         self.mark=mark
#
#
# st1=Student("anu",1,"bca",200 )
# st2=Student("rahul",2,"bba",177 )
# st3=Student("vinod",3,"bba",187  )
# st4=Student("ajay",4,"bca",198  )
# st5=Student("maya",5, "bba",195 )
# if st1.mark>st2.mark and st1.mark>st3.mark and st1.mark>st4.mark and st1.mark>st5.mark:
#     print(st1.name,st1.rollno,st1.mark,st1.school)
# elif st2.mark>st3.mark and st2.mark>st4.mark and st2.mark>st5.mark:
#     print(st2.name, st2.rollno, st2.mark, st2.school)
# elif st3.mark>st2.mark and st3.mark>st4.mark and st4.mark>st5.mark:
#     print(st3.name, st3.rollno, st3.mark, st3.school)
# elif st4.mark>st2.mark and st4.mark>st3.mark and st4.mark>st5.mark:
#     print(st4.name, st4.rollno, st4.mark, st4.school)
# else:
#     print(st5.name, st5.rollno, st5.mark, st5.school)


#7
# import re
# f=open("phoneNumber","r")
# r="[+][9][1]\d{10}"
# for i in f:
#     val=i.rstrip('\n')
#     matcher=re.fullmatch(r,val)
#     if matcher is not None:
#         print(val)

#8
# try:
#     if 1/0:
#         print("hello")
# except:
#     print("except")
# finally:
#     print("finally")


#9
# import re
# x=input("enter the string")
# rule="^[A-Z]\w{3,8}[A-Z]$"
# matcher=re.fullmatch(rule,x)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")

#11
# import re
# x=input("enter the string")
# rule="^a\d+b$"
# matcher=re.fullmatch(rule,x)
# if matcher is not None:
#     print("valid")
# else:
#     print("not valid")

# class Person:
#     def details(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
#
# p=Person()
# p.details("hai")
# print(p)
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class Employee(Person):
#
#     def __init__(self,name,age,cname):
#         super().__init__(name, age)
#         self.cname=cname
#
# e=Employee("name",12,"abc")
# print(e.cname)


# prime or not


