#filter(fun, list)
#fun must return true or false only

list1 = [1,2,3,4,5,6,7,8]
even = list(filter(lambda value:value%2==0, list1))
print(even)


products = [
    {"name":"shoes", "price":1200},
    {"name":"shirts", "price":2200},
    {"name":"pants", "price":1500},
    {"name":"shoes", "price":1000}
]

shoes =  list(filter(lambda item:item["name"] == "shoes",products))
print(shoes)



