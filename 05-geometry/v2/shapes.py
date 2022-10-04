import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi + (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def perimeter(self):
        return self.circumference()


class SquaredCircle(Shape):
    def __init__(self, w):
        self.square = Rectangle(w, w)
        self.circle = Circle(w/2)

    def area(self):
        return self.square.area()

    def perimeter(self):
        return self.square.perimeter()


class Drawing:
    def __init__(self):
        self.shapes = []

if __name__ == '__main__':
    shapes = []
    shapes.append(Rectangle(4, 5))
    shapes.append(Rectangle(6, 2))
    shapes.append(Circle(6))
    shapes.append(Rectangle(10, 3))
    shapes.append(Circle(3))

    for shape in shapes:
        print(type(shape), shape.perimeter())

