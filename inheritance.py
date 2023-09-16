
# Pet: Parent, baseclass
# Cat, dog: Child, subclass
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and my age is {self.age}")

    def speak(self):
        print("I dont know what to say")
    
    def __str__(self):
        return self.name

class Cat(Pet):
    def __init__(self, name, age,  color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow meow..")


# cat1 = Cat("Tim", 8)

class Dog(Pet):

    def speak(self):
        print("Bark bark..")


class Fish(Pet):
    pass


cat2 = Cat("Alice", 12, "gray")
print(cat2)

cat2.speak()


f = Fish("bob", 2)
f.speak()

dog = Dog("eric", 1)
dog.speak()

dog.show()
