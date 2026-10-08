class Student:
    def __init__(self,phy, chem,math):
        self.phy=phy
        self.chem=chem
        self.math = math
    @property #it makes total as propery attribute of object to call total we call like s1.total not like s1.total()
    def total(self):
        return self.phy + self.chem + self.math

s1=Student(10,20,30)
print(s1.total)


#define a circle class to create a circle withr readius r using the constructor
#define an Area() methode to calculate the area of circle using @property
#define a Perimeter() methode to calculate the perimeter of circle


""" class Circle :
    def __init__(self,r):
        self.r=r     
    @property
    def Area(self):
        return 3.14*self.r*self.r

    def Perimeter(self):
        return 2*3.14*self.r

c1 = Circle(10)
print(c1.Area)
print(c1.Perimeter()) """