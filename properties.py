class Product:
    def __init__(self, price):
        self.__price = price
    
    @property
    def price(self): # getter
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Negatif deger giremezsiniz")
        self.__price = value

    
        
product = Product(10)
# product.price = -10
# product.set_price(10)

# print(product.get_price())


print(product.price)
product.price = 2



