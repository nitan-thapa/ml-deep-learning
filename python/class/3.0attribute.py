#attribute
#class attribute 
    #those attribute which is common to all instance(object) are placed in class attribute
    #it is shared by all instance (object) of class
    #can be accessed throw class or instance
#instance attribute (object attribute)
    #it is unique for each instance
    #has different memory for each instance
    #can be accessed only by instance
    #it is define in __init__ method

#use diagram 

class Student:
    college = "deerwalk"
    address="sifal"
    def __init__(self,name,age):
        self.name=name#(for different object differen memoroy will be created)
        self.age = age#(for different object differen memoroy will be created)



print(Student.college)
print(Student.address)

obj1 = Student("ram",31)#{name:"ram",age:31}
print(obj1.name)
print(obj1.age)

obj2 = Student("nitan",32)#{name:"nitan",age:32}
print(obj2.name)
print(obj2.age)

# print(Student.name)  #it throw an error as instances attribute can not access class attribute





