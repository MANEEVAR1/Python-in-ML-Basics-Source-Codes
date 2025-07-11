# OOPS 
# Class => Blueprint eg: Car design
# Oject => Instance of class eg: Tesla, Audi, BMW

class Student:
    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Show(self):
        print(f"Hello World, I am {self.name} and I am {self.age} years old.")

ABC = Student("Moksh",20)
ABC.Show()


# 4 Main Pillers of OOPS:
# Inheritance
# > single inheritance
# > multiple inheritance
# > multilevel inheritance
# > hierarchical inheritance
# > hybrid inheritance


class Animal: # Parent class
    def speak(self):
        print("Animal can speak")

class Dog(Animal): # Child class + parent class
    def bark(self):
        print("Dog can bark")

class John(Animal): # Child Class of Animal
    def run(self):
        print("John can run")

a = John()
a.speak()  # Inherited method from Animal class
a.run()    # Method from John class

dog1 = Dog()
dog1.speak()  # Inherited method from Animal class
dog1.bark()   # Method from Dog class


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Polymorphism 
class Bird:
    def sound(self):
        print("Birds can sound")

class Parrot(Bird):
    def sound(self):
        print("Parrots can mimic sounds")

class Sparrow(Bird):
    def sound(self):
        print("Sparrows can chirp")

for bird in (Parrot(), Sparrow()):
    bird.sound()


# >>>>>>>>>>>>>>>>> Encapsulation
class car:
    def __init__(self):
        self.__maxspeed = 200 # Private variable

    def drive(self):
        print(f"Driving at max speed of {self.__maxspeed} km/h")

car1 = car()
car1.drive()


# >>>>>>>>>>>>>>>>> Abstruction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()  # Output: Bark

cat = Cat()
cat.sound()  # Output: Meow









# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
Q1. Student Report System (Class, Object, Encapsulation)
Create a class Student with:
Private attributes: __name, __marks
A method set_details(name, marks)
A method get_result() to print pass/fail (pass if marks >= 40)
 
# Sample Output:
# Name: Ram
# Marks: 85
# Result: Pass

Q2. Animal Kingdom (Inheritance + Polymorphism)
Create a base class Animal with method speak()
Then create 2 subclasses:
Dog → speak() should print "Barks"
Cat → speak() should print "Meows"
Loop through list of objects and call speak() to show polymorphism.
 
# Sample Output:
# Barks
# Meows

Q3. Payment Gateway (Abstraction + Inheritance + Method Overriding)
Use abc module.
Create abstract class Payment with abstract method make_payment().
Create subclasses:
CreditCard → prints "Paid using credit card"
UPI → prints "Paid using UPI"
 
# Sample Output:
# Paid using credit card
# Paid using UPI

'''
