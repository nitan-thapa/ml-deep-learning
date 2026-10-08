#map is used to convert 

# map(fun,list)


lis = [1,2,3]

""" def fun(el):
    return el*2
double = list(map(fun,lis))
print(double) """


#or

double  =list( map(lambda el:el*2, lis))
print(double)

#or 
upper = list(map(lambda el:el.upper(), ["nitan","ram"]))
print(upper)