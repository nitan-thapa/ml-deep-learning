#class method 
#it is define insidie teh class
#can be call by class name and object name (same as normal)
#it has access to class attribute and class methode
#it has no access to object attribute and object method


class Person:
    name="anonymous"
    def __init__(self,name):
        self.name=name

    def changeObjAtt(self,name):#instance methode
        self.name=name
    @classmethod 
    def changeClassAtt(cls,name):#class methode
        cls.name=name
    


p1=Person("nitan")#{name:"nitan"}
print(p1.name)#nitan
print(Person.name)#anonymous 

p1.changeObjAtt("roshan")
print(p1.name)#roshan
print(Person.name)#anonymous 

p1.changeClassAtt("ram")
print(p1.name)#roshan
print(Person.name)#"ram"
Person.changeClassAtt("hari")
print(Person.name)#"hari"




