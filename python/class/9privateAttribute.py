#private attributes and methode
#private attributes and methode are not accessible outside the class
#to make any attribute and methode as private just prefix its name by __
#both class an object have priveate attribute and methode
class Student :
    __college="nec"
    def __check(self):
        print("check")
    def call(self):
        print(self.__college)#we can access private attribute and methode in class itself
        self.__check()


s1=Student()
# print(s1.__college) # it throw an error because __college is private
# s1.__check()#it throw an error because __check is private
# print(Student.__college) #it throw an error
s1.call()