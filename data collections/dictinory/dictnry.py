dict1 = {'name': 'ananthu', 'age': '23'}
print(dict)
print(type(dict))


#mutable
# hetrogeneous




print(dict1['name'])

dict2 = {}
dict1['age'] = 15  # updating an existing element
dict1['school'] = "hello"  # Add a new entry
dict1.update({"location": "thazhava"})
print(dict1)

del dict1['age']  # remove an element

dict1.clear()  # clear

del dict1  # del



a = {1: 2, 2: {2: 7}}
print(a)
