
#while getting first get position argument then keyword argument 
#all position argumnt is get by * 
#all keyword argument is get by **
def fun(name, *args, last_name, **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


fun("nitan",1,2,last_name="ram", age=31, city="kathmandu")
#while passing first pass position argument then key work argument