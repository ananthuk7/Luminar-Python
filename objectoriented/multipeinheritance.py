class Person:
    def pdetails(self, name, age):
        self.name = name
        self.age = age


class Student:
    def sdetails(self, name, age):
        self.name = name
        self.age = age


class Employee(Person, Student):
    def edetails(self, id, salary):
        self.id = id
        self.salary = salary
