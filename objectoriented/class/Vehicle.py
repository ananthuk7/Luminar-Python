class Vehicle:
    def __init__(self, name, model, color, types):
        self.name = name
        self.model = model
        self.color = color
        self.type = types

    # to string method ==> it returns string amd itr returns the value instead of object reference
    def __str__(self):
        return self.name


ve = Vehicle("maruthi", 1000, "black", "4 wheeler")
print(ve)
ve1 = Vehicle("maruth", 1000, "black", "4 wheeler")
print(ve1)
