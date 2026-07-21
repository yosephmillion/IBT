#Exercise 1
class Report:
    def __init__(self, content):
        self.content = content


class ReportSaver:
    def save(self, report):
        print(f"Saving report: {report.content}")


class ReportEmailer:
    def email(self, report):
        print(f"Emailing report: {report.content}")


report = Report("Monthly Sales Report")

saver = ReportSaver()
emailer = ReportEmailer()

saver.save(report)
emailer.email(report)

#Exercise 2
from math import pi


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Square(4),
    Triangle(6, 3)
]

for shape in shapes:
    print(shape.area())

#Exercise 3
class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


a = AppSettings()
b = AppSettings()

print(a.currency)
print(a is b)

#Exercise 4
class Circle:
    pass


class Square:
    pass


class Triangle:
    pass


class ShapeFactory:

    @staticmethod
    def create(kind):
        if kind == "circle":
            return Circle()
        elif kind == "square":
            return Square()
        elif kind == "triangle":
            return Triangle()
        else:
            raise ValueError("Unknown shape")


shape = ShapeFactory.create("circle")
print(type(shape).__name__)

#Exercise 5
class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class TVChannel:
    def update(self, news):
        print(f"TV: {news}")


class Newspaper:
    def update(self, news):
        print(f"Newspaper: {news}")


agency = NewsAgency()

agency.subscribe(TVChannel())
agency.subscribe(Newspaper())

agency.notify("Python 3.15 Released!")