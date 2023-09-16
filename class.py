numbers = [1,2]

x = 1

print(type("hello"))

print(type(x))

def f_hello():
    print("hello!")


print(type(f_hello))

x = 2
y = "hello"

# print(x+y)

# print(x.upper())

# class : blueprint for reating new objects/instances in python

# class : Human
# objects : sila, ebrar, ugur

class Point: # pascalcase
    def draw(self):
        print("draw..")

point1 = Point()

point1_isinstance_Point = isinstance(point1, Point)
print(point1_isinstance_Point)
print("*" * 30)
point1_isinstance_int = isinstance(point1, int)
print(point1_isinstance_int)

print(type(point1))

class Dog:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def add_one(self, x):
        return x+1
    
    def bark(self):
        print(f"bark .. {self.name}, {self.age}")

    def __str__(self):
        return f"{self.name}"
    
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    

d1 = Dog("Tim", 19)
# print(type(d1))

d2 = Dog("Alice", 2)
d1.bark()

print(f"d1 age: {d1.age}")
print("*" * 30)
d1.set_age(13)

print(f"d1 new age: {d1.age}")

d1.color = "brown"

print(d1.color)

