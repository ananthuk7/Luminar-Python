class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, eid, salary, name, age):
        super().__init__(name, age)
        self.eid = eid
        self.salary = salary

    def pri(self):
        print(self.eid, self.name, self.age, self.salary)


c = Employee(100, 2000, "anu", 23)
c.pri()
