
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Woof")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Mieow")


if __name__ == '__main__':
    a = Dog("Pluto")
    b = Cat("Sylvester")

    a.sound()
    a.eat()

    b.sound()
    b.eat()