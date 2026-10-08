

class Student:
    name="nitan" ##class attribute  (it is shared by all object) take one common memory)
    age = 31 ##class attribute  (it is shared by all object) take one common memory)
    def __init__(self,name):
        self.name=name#(for differen object differen memoroy will be created)


print(Student.name)#"nitan"
print(Student.age)

obj1 = Student("ram")#{name:"ram"}
print(obj1.name)#first it looks in its own memory if it does not find then it looks in class memory
print(obj1.age)

print(Student.name)
print(Student.age)


