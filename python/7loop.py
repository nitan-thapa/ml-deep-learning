#for loop with list,tuple,set 
""" for el in [1,2]:
    print(el)#1 2 """

""" for el in (1,2):
    print(el)#1 2 """

""" for el in {1,2}:
    print(el)#1 2 """

# for loop with string
""" for el in "nitan":
    print(el) """


#for loop with enumerate 
""" for i, value in enumerate(["a","b"]):
    print(i,value) """



#for loop with dictionary items
# info = {"name":"nitan","age":31}
""" for el in info.keys():
    print(el) """

""" for el in info.values():
    print(el)#nitan 31 """

""" for key,value in info.items():
    print(key,value) """


#for loop with range 
# range(start, end,step) ,end is exluded
#by default step is 1

""" for el in range (1,3): 
    print(el) """



#while loop 
#python has for loop and while loop only
#it does not have do whle loop 
#while(condtion):
    #statement

#printing number form 1 to 5
i =1
while(i<=2):
    print(i)
    i=i+1


#no need
#break and continue
#break break whole iteration of a loop
#continue break the given iteration and continue next iteraion
