
class Person:
    num_of_people = 0
    GRAVITY = -9.8 

    def __init__(self, name):
        self.name = name
        self.add_person()


    @classmethod
    def number_of_people(cls):
        return cls.num_of_people
    
    @classmethod
    def add_person(cls):
        cls.num_of_people += 1




p1 = Person("Tim")
# print(f"p1 added, num of people: {p1.num_of_people}")
print("*" * 30)
p2 = Person("Alice")
# print(f"p2 added, num of people: {p2.num_of_people}")

print(p1.number_of_people())

print(f"Peeople Number {Person.number_of_people()}")