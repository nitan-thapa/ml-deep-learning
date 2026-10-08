# * is just like rest operator
#* is always place at last 
#* it takes all rest of value

def fun(a,b,*c):
    #it takes  argument in the form of tuple 
    print(a,b,c)#c is (3,4,5,6,7,8)

fun(1,2,3,4,5,6,7,8)


a,b,*c = (1,2,3,4,5,6)
print(a,b,c)
# c is [3,4,5,6]  it takes in the form of list

a,b,*c = [1,2,3,4,5,6]
print(a,b,c)#c is [3,4,5,6] 

""" def fun1(a,b,*args):#you must give value fro a and b , *args is rest operation it is not necessary to give value
    print(a, b, args)  

# fun1(1)  #Error
fun1(1,1) #1 1 () """