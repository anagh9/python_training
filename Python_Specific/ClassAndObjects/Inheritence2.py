# Constructor with Super Method or Call Parent Class Constructor in Child Class in Python 

# If we write constructor in the both classes, parent class and child class then the parent class constructor is not avialable to the child class. 
# In this casr only child class constructor is accessible which means child class constructor is replacing parent class constructor 

# super() method is used to call parent class constructor or methods from the child class .


class Parent:
    def __init__(self) -> None:
        print("Father Class Construcctor")
    
    def show(self):
        print("Father Class Instace Method")

class Son(Parent):
    def __init__(self) -> None:
        super().__init__() # Parent Class Constructor
        print("Son class Constructor")
    
    def disp(self):
        print("Son Class Instance Method")


c = Son()
# Output
# Father Class Construcctor
# Son class Constructor


# Link (Multiple Inheritence) - https://www.youtube.com/watch?v=rYUGnVPOih4&list=PLbGui_ZYuhijd1hUF2VWiKt8FHNBa7kGb&index=27&ab_channel=GeekyShows