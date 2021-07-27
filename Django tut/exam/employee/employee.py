fp = open("employ", "r")
emp = {}


def employee_details(id1, data1=""):
    flag = 0
    for i in fp:
        data = i.rstrip('\n').split(" ")
        emp["id"], emp["name"], emp["desig"], emp["desig"], emp["salary"] = data[0], data[1], data[2], data[3], data[4]
        if emp["id"] == id1 and emp["desig"] == data1:
            print(emp["name"], emp["desig"])
            break
        elif emp["id"] == id1 and emp["desig"] == data1:
            print(emp["name"], emp["exp"])
            break
        elif emp["id"] == id1 and emp["desig"] == data1:
            print(emp["name"], emp["salary"])
            break
        elif emp["id"] == id1:
            print(emp['name'])
            break
        # else:
        #     print("not valid")


employee_details("1001", "developer")
