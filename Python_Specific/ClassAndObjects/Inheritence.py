class Parent:
    money = 1000

    def __init__(self) -> None:
        print("Parent Called")

    def instance_fun(self):
        print("Instance Function")

    @classmethod
    def class_fun(cls):
        print(cls.money)
        return cls.money

    @staticmethod
    def static_fun(a, b):
        print(a+b)


class Student(Parent):
    def __init__(self) -> None:
        self.money = 50000
        print("Son Class Called")
    pass


# Constructor Overriding
p = Student()

print(p.class_fun())
p.static_fun(1, 2)
p.instance_fun()
