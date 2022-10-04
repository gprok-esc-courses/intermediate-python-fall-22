import math


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi + (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    shapes = []
    shapes.append(Rectangle(4, 5))
    shapes.append(Rectangle(6, 2))
    shapes.append(Circle(6))
    shapes.append(Rectangle(10, 3))
    shapes.append(Circle(3))

    for shape in shapes:
        if isinstance(shape, Rectangle):
            print(type(shape), shape.perimeter())
        elif isinstance(shape, Circle):
            print(type(shape), shape.circumference())

