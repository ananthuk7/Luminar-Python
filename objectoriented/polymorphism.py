# polymorphism means many forms
# overloading .. same method but different arguments
# and python doesnt support method over-loading

# over-riding...same method name and same number of arguments
# child class override parent class method




#overoading

class Operator:
    def num(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(self.n1, self.n2)


class Display(Operator):
    def num(self, n1):
        self.n1 = n1
        print(self.n1)


d = Display()
d.num(5)

# over-riding
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

