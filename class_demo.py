class Parent:
    pass


class Child(Parent):
    i = 100  # class/static variable

    def __init__(self, x):  # constructor of class
        self.x = x  # instance variable

    def f():  # class/static method
        return 'Hi OOP'

    def ff(self):  # instance method
        return self.x


print(Child.i)
print(Child.f)
print(Child.f())
print(Child.ff)
# print(Child.ff())
obj = Child(120)
print(obj.ff())
# print(obj.f())
