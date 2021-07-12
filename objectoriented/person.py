#constructors


class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printVal(self):
        print(self.name,self.age,self.address)

obj=Person("ananthu",23,"abc")
# obj.printVal()