class Student:
    @staticmethod
    def fun(a,b):
        print("this is static method")
        print(a,b)

print(Student.fun(1,2))