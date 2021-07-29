fp = open("employ", "r")
emp = {}

# def employee_details(id1, data1=""):
#
#     for i in fp:
#         data = i.rstrip('\n').split(" ")
#         emp["id"], emp["name"], emp["desig"], emp["desig"], emp["salary"] = data[0], data[1], data[2], data[3], data[4]
#         if emp["id"] == id1 and emp["desig"] == data1:
#             print(emp["name"], emp["desig"])
#             break
#         elif emp["id"] == id1 and emp["desig"] == data1:
#             print(emp["name"], emp["exp"])
#             break
#         elif emp["id"] == id1 and emp["desig"] == data1:
#             print(emp["name"], emp["salary"])
#             break
#         elif emp["id"] == id1:
#             print(emp['name'])
#             break
#         # else:
#         #     print("not valid")
#
#
# employee_details("1001", "developer")
for i in fp:
    data = i.rstrip('\n').split(" ")
    id1 = data[0]
    name = data[1]
    desig = data[2]
    exp = data[3]
    salary = data[4]
    emp[id1] = {"id": id1, "name": name, "desig": desig, "exp": exp, "salary": salary}


# for k, v in emp.items():
#     print(k, v)
def employ_details(**kwargs):
    if kwargs["id"] == emp.get("id"):
        print(emp["id1"]["name"])


employ_details(id="1001")