

class Test:
    name = "John"
    objects_created = 0

    def __init__(self, n, a):
        self.name = n
        self.age = a
        Test.objects_created += 1

    @classmethod
    def check(cls):
        print(cls.name)


user = Test("Peter", 34)
print(user.name)
user.check()

user2 = Test("Mary", 28)

print(user.name)
user.check()

print(Test.objects_created)




