fp = open("employ", "r")
emp = {}
for line in fp:
    id1, name, desig, exp, salary = line.rstrip('\n').split(" ")
    emp[id1] = {"id": id1, "name": name, "desig": desig, "exp": exp, "salary": salary}


# print(emp)

def print_emploayee(id=None, **kwargs):
    if id in emp:
        print(emp[id]["name"])
        try:
            if "props" in kwargs:
                print(emp[id][kwargs["props"]])
        except:
                print("invalid property")
    else:
        print("invalid id")




print_emploayee("1000",props="salar")
