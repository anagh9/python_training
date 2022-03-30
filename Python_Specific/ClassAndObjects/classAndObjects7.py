# Access Modifier
class Public:
    name = "ANAGH KUMAR"

    def __init__(self) -> None:
        pass

    def getName(self):
        return self.name


class Protected:
    _name = "ANAGH KUMAR"

    def __init__(self) -> None:
        pass

    def getName(self):
        return self._name


class ProtectedSubclass(Protected):
    def __init__(self) -> None:
        super().__init__(self)

    # def printName(self):
        # return self._name


class Private:
    __name = "ANAGH KUMAR"

    def __init__(self) -> None:
        pass

    def getName(self):
        return self.__name


obj1 = Public()
print(obj1.name)  # ANAGH KUMAR
obj2 = Protected()
print(obj2.getName())  # ANAGH KUMAR
print(obj2._name)  # ANAGH KUMAR
# print(obj2.printName())

obj3 = Private()
print(obj2.getName())  # ANAGH KUMAR
# print(obj2.__name) # Error
