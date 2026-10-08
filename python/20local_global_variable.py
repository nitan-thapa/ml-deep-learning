x=5 #global varible

def fun1():
    x=1#local variable (it does not change global variable)
    

def fun2():
      
      global x #it means x is global
      x=10 #it change global variable
   
print(x)#5
fun1()
print(x)#5  
fun2()
print(x)#10