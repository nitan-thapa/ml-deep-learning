#tuple
#it is just like list but it is immutable it means we can not assign items


#defining tuple
t1 = ("a","b",1)
t2 = "c","d","e"
t3 = ("e",) #tuple of one element
data = ("e")#it is same as "e"

print(t1,t2,t3,data)

#gettin tuple 
t1 = ("a","b",1)
#      0,  1,  2
#      -3 ,-2 , -1
print(t1[0],t1[1],t1[2])
print(t1[-1],t1[-2],t1[-3])

#changing tuple
#t1[2]=3 # it throw an error


#converting  tuple to list 
t1 = ("a","b",1)
print(list(t1))


#converting list to tuple 
l1 = ["a","b",1]
print(tuple(l1))




