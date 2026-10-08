#inheritance
#inheritance is the process of inherting the properties of one  class to another calss
#parent class is called base class
#child class is called derived class
""" class Car :
    def check(self):
        print("check")

    def start(self):
        print("start")
    def stop(self):
        print("stop")
    tire=4 

class ToyotaCar(Car):
    pass

t1= ToyotaCar()
t1.check()
t1.start()
t1.stop()
print(t1.tire) """



#types of inheritance
#single inheritance    base=> derived   (single base and singe defived)
#mutiple inheritance   derive class is made from multiple base class
#multi level inheritance   base=> derived1=> defived2...


#example of multiple inheritance 
# class A:
#     varA="i am varA"
# class B:
#     varB="i am varB"
# class C(A,B):
#     varC="i am varC"
# c1= C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)



#multi level inheritance   base=> derived1=> defived2...
class Car:
    def check(self):
        print("check")
    def start():
        print("car started")
    def stop():
        print("car stopped")
    tire=4

class ToyotaCar(Car):
    energy="petrol"

class Fortuner(ToyotaCar):
    pass

f1= Fortuner()
f1.start()
print(f1.energy)
