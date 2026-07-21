#Exercise 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author} - {self.pages} pages")


book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Python Crash Course", "Eric Matthes", 544)

book1.describe()
book2.describe()

#Exercise 2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


product = Product("Laptop", 50000, 10)

product.restock(5)
product.sell(3)

print(product.quantity)

#Exercise 3
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n


product = Product("Phone", 25000, 8)

print(product.quantity)

#Exercise 4
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        if n > self.quantity:
            raise ValueError("Not enough stock.")
        self.quantity -= n


product = Product("Tablet", 18000, 5)

product.sell(2)
print(product.quantity)

#Exercise 5
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


p1 = Product("Mouse", 500, 20)
p2 = Product("Keyboard", 1200, 15)
p3 = Product("Monitor", 9000, 5)

p1.sell(5)

print(p1.name, p1.quantity)
print(p2.name, p2.quantity)
print(p3.name, p3.quantity)
