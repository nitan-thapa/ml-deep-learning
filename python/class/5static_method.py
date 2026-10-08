#static method
class Student:
    @staticmethod #you must prefix by @staticmethod to make any function static
    def fun():
        print("this is static method")

#static munctin does not have self
s1 = Student()
s1.fun()
Student.fun()

""" 
note both normal method and staic methode are class method

 """

""" 
normal methode
    it has self
    it means it has access to object attribute

satic methode 
    it does not have self
    it means it can access teh object attribute

 """


    