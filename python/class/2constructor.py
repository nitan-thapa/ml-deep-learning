#constructor
#they are the function which is called automatically when object is created
#its name must be __init__(self)
#self point its own object

class Student: 
    def __init__(self):#self points its own object
        print("this is constructor")

obj = Student()



#paratamerixed contructor 
class Product:
    def __init__(self,name,price):#it is named becauses it is used to initialize
        print(name,price)

obj = Product("laptop",1000)

