#it is the parent class which tells this methode is compulsary in child class

from abc import ABC, abstractmethod

class Animal(ABC):#this is the abstract class, we cant create abastract class objec
    species="Animal"
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
     name="benju"
     def sound(self):
            print("bark")

d1 = Dog()
d1.sound()
print(d1.species,d1.name)
#if sound methode is missing it will give error