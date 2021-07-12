class Operator:
    def num(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(self.n1, self.n2)

    def num(self, n1):
        self.n1 = n1
        print(self.n1)


d = Operator()
d.num(5)
