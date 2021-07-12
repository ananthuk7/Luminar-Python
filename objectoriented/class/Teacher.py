class Teacher:
    college_name = "something"

    def __init__(self, name, tid, dep, sub):
        self.name = name
        self.tid = tid
        self.dep = dep
        self.sub = sub

    def printd(self):
        print(self.name, self.tid, self.sub, self.dep, Teacher.college_name)


# te1 = Teacher("anu", 3, "cs", "python")
# te1.printd()
for i in range(0,3):
    tei = Teacher(input("name"), int(input("age")), input("name"), input("name"))
    tei.printd()




