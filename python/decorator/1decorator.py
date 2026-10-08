#decorator is a function that takes argument as function 
#and return new function which is modified version of original function




def decorator_func(fun ):
    def inner():
        print("this is before function")
        fun()
        print("this is after function")
    return inner



@decorator_func
def sum():
    print("this is sum function")

def add():
    print("this is add function")

sum()