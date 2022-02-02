"""
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
"""

def myfun(*arg):
    print(arg[0]) # [2, 3, 4, 5, 6, 1, 1]
    print(arg[1]) # [2]
    print(arg[2]) # (2,)
    a = list(arg[2])
    a[0] =4
    a = tuple(a)
    print(a) # (4,)

myfun([2,3,4,5,6,1,1],[2],(2,)) 


def myFun(*argv):
    for arg in argv:
        print (arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
myFun({'1':"44"},{'3':'34'})
"""
Output :
Hello
Welcome
to
GeeksforGeeks
"""

########################################################
"""
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

- A keyword argument is where you provide a name to the variable as you pass it into the function.

- One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""
def myFunction(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFunction(first ='Geeks', mid ='for', last='Geeks')   


def sourabh(a,*k):
    print(a)
    print(k)

sourabh(34,434,3434,2334,54,45)