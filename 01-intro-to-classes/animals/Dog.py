
class Dog:
    def __init__(self, name):
        print("constructor called")
        self.name = name

    def bark(self):
        print(self.name + " says Wooof")

    def rename(self, name):
        self.name = name;

    def __str__(self):
        return "Dog named " + self.name



a = Dog("Pluto")
a.rename("Peter")
a.bark()


b = Dog("John")
b.bark()

c = a
c.bark()

print(a)
print(b)
print(c)