#you can access class attribute by using object 
#but you can not change it , delete it using  object but you can change it through class

class Student:
    college="nec"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def check(self):
        print("check")

s1 = Student("ram",31)

#get attribute 
print(s1.name, s1.age, s1.college)
#get method
s1.check()

#changing attribute 
s1.name = "ram"
s1.age = 32 
#s1.college ="Nepal Engineering college" #it does not change class attribute , it change object attribute
print(s1.name, s1.age, s1.college)
print(Student.college)#nec

#changing method
s1.check =lambda : print("check1")#it does not change class but ti affect object
s1.check()
Student.check(s1)

#deleting attribute 
del s1.name
del s1.age
# del s1.college   #it throw an error as object can not delete class attribute
# print(s1.name, s1.age, s1.college)