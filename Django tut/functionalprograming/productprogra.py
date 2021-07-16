products = [
    {"item_name": "boost", "mrp": 290, "stock": 50},
    {"item_name": "complan", "mrp": 240, "stock": 10},
    {"item_name": "bournvita", "mrp": 320, "stock": 20},
    {"item_name": "horlicks", "mrp": 280, "stock": 13},
    {"item_name": "nutricharge", "mrp": 275, "stock": 0},
]

# list all product names
# pd=list(map(lambda product:product["item_name"],products))
# print(pd)


# out of stock
# pd = list(filter(lambda product:product["mrp"]==0,products))
# print(pd)

# #highest cost
# from functools import  reduce
#
# prices=list(map(lambda product:product["mrp"],products))
# highc=reduce(lambda p1,p2 :p1 if p1> p2 else p2,prices)
# print(highc)
