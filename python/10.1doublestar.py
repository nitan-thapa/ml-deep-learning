#* takes rest of position argument 
#** takes rest of key word argument in the form of dictionary


def fun1(name,**kwargs):
    print(name,kwargs)#kwargs {"age":31,"country":"nepal"}

fun1(name="nitan",age=31,country="nepal")