class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.length * self.width
    
    @property
    def length(self): #get
        return self.__length

    @length.setter
    def length(self, value): #set
        if value <= 0 :
            raise ValueError("Uzunluk neg ya da 0 olamaz")
        self.__length = value

    @property
    def width(self): #get
        return self.__width
    
    @width.setter
    def width(self, value): #set
        if value <= 0 :
            raise ValueError("Uzunluk neg ya da 0 olamaz")
        self.__width = value

    

rec = Rectangle(5, 10)
print(rec.length, rec.width)
rec.length = 10
rec.width = 2
print(rec.length, rec.width)

print(rec.area())
print("*" * 30)

rec.length = 20
print(rec.area())