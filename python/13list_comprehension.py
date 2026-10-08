#list comprehension  (it has three version)
# [return_value  for_in_loop]    (without if else)
#[return_value  for_in_loop if_condition] ( with only if)
#[Ternary_operator  for_in_loop] 

l1 = [ i*2 for i in [1,2]]#[1,4]
print(l1)


""" names = ["nitan", "ram"]  #print ["nitan thapa","ram thapa"]
l2 = [ f"{el} thapa" for el in names] #["nitan thapa" "ram thapa"]
print(l2)
 """



""" l= ["abc", "dev"] #["cba", "ved"]
l2 = [ el[::-1]   for el in l]
print(l2)
 """ 


""" #printing even number 
l1= list(range(1,11))
even= [el for el in l1 if el%2==0]
print(even) """



""" #filtering all int and float value  (note int and float are not wrap by ""  as they are class)
l1 = [True, 1, (1,2), 2.31, 4]
l2 = [ el  for el in l1 if(type(el)==int or type(el)==float)]
print(l2)   """



""" #print even or odd list
l1 = list(range(1,11))
l2 = [ "even" if(el%2==0) else "odd" for el in l1 ]
print(l2) """



""" l1 = ["male", "female", "other", "male", "other"]
l2 = ["He" if(el=="male") else "she" if(el=="female") else "they" for el in l1]
print(l2) """



products = [ 
    {"name":"laptop", "price":100000, "quantity":10},
    {"name":"mobile", "price":700000, "quantity":5},
    {"name":"tablet", "price":500000, "quantity":3}
]

#  ["laptop", "mobile", "tablet"]