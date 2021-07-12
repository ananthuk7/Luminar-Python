class Person:
    def printVal(self,name):
        self.name=name
        print(self.name)

class Child(Person):
    def printVal(self,name):
        self.name=name
        print(self.name)

c=Child()
c.printVal("name")
