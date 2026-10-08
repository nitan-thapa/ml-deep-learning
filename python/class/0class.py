#defining class
#it is good to make first letter of class as capital
#while defining class never seperate attribute with comma

class Student: #first letter of class must be capital
    collage_name = "deerwalk"#collage_name is attribute 
    address = "kathmandu"

#get Student attribute
# print(Student["collage_name"])   #it will give error
print(Student.collage_name)
print(Student.address)


#change Student attribute 
Student.collage_name = "deerwalk compare"
print(Student.collage_name)#deerwalk compare


#printing whole class
print(Student)

