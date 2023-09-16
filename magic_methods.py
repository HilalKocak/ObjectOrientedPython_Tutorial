class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
       return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x},{self.y}"


point = Point(1,1)
other = Point(2,2)

print(point == other)

print("*" * 30)

# print(point > other)
print(point < other)


print(point + other)

combined = point + other
print(combined.x, combined.y)