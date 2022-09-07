
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


if __name__ == '__main__':
    a = Rectangle(8, 3)
    print(a.area())
    print(a.perimeter())
