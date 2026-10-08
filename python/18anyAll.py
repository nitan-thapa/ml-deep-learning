""" print(any([True,False,True]))#True if any value is truthy value
print(any(["",False,0]))#False, 
 """


""" print(all([True,True,True]))#True if all value is truthy value
print(all([False,True,True]))#False """



l= [2,4,6,1]

#check if all are even 
is_all_even = all([ el%2==0 for el in l])
print(is_all_even)


#chek if any one is minor
l = [1, 20, 25]

is_any_one_minor =any( [el<=18 for el in l])
print(is_any_one_minor)