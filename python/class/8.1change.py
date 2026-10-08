# object can change object attribute but can not change class attribute

class Student :
    school_name = "deerwalk"
    def __init__(self ):
        self.name = "nitan"
    def change(self):
        self.name = "ram"
        self.school_name = "compare" #it does not change the class attribute, but makes new object attribute
        


S1 = Student()
S1.change()

print(S1.name)
print(S1.school_name)
print(Student.school_name)

