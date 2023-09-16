class Animal(): #Baseclass
    def eat(self):
        print("eat")


class Bird(Animal): #subclass
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass

bird = Bird()

print(isinstance(bird, Chicken))

animal = Animal()

print(isinstance(animal, object))

print(issubclass(Bird, Animal))

class Employee:
    def greet(self):
        print("Employee Greet ")


class Person:
    def greet(self):
        print("Person Greet ")


class Manager(Employee, Person):
    def greet(self):
        print("Manager Greet")

manager = Manager()
manager.greet()

 
