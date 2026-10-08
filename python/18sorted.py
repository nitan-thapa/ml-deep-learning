#ascending sort

#ascending sort
l1 = [2,3,1]
s1 = sorted(l1)
print(s1)

#descending sort
l1 = [2,3,1]
s1 = sorted(l1,reverse=True)
print(s1)



students = [
    {"name":"ram", "marks": 80},
    {"name":"hari", "marks": 70},
    {"name":"nitan", "marks": 90},
]




s1 = sorted(students,key= lambda item:item["marks"])
#meaning sort studetns 
print(s1)

#sort according to length 
s1 = sorted(students,key = lambda item:len(item["name"]))
print(s1)



#sorted outpput is in list
print(sorted("nitan")) 


