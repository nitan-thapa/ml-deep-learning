

#super function
#super function is used to call the parent class methode and attribute in child class


class C:
    def __init__(self):
        print("this is class C")
    varA="i am varC"
class A(C):
    def __init__(self):
        print("this is class A")
    varA="i am varA"

class B(A):
    varA="i am varB"
    def __init__(self):
        print("this is class B")
        super().__init__()
        print(self.varA)#i am varB
        print(super().varA)#i am varA
        print("i am init of B")

b1= B()