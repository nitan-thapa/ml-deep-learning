#method is a function  of a class(memory)
class Student:

    def fun (self,name,age):#self points itself
        print(name)#self["name"] it does not works
        print(age)
        
obj = Student()
obj.fun("ram",31)

#if you want to call it by using classNameu
# Student.fun(obj,"ram",31) #you have to pass one object