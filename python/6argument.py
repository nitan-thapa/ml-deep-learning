#position argument  
    #position matter
#key word argument
    #position does not matter
    #but all keyworkd argument must come after position argument


#position argument 
# (first is taken by first, second by ...)
#order is importan
def info(name,age ,country,city):
    print(name,age,country,city)

info("nitan", 31, "nepal", "kathmandu")

#keyword argument 
#order not importan
info(city="kathmandu",name="nitan", age=31, country="nepal", )


#combination of both 
info("nitan", 31,  city="kathmandu",country="nepal")
#info(city="kathmandu","nitan" ,age=31, country="nepal") #this give error because keyword argument must come after position argument
