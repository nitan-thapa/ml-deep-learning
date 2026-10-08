

# decorator with parameter
def decorator_func(fun ):
    def inner(a,b,c):#we take argument in this place
        print("this is before function")
        fun(a,b,c)
        print("this is after function")
    return inner



@decorator_func
def sum(a,b,c):
    print("this is sum function")
    print(a,b,c)

sum(1,2,3)
