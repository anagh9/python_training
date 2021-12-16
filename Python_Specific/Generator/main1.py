# Generator Expression

"""
In Python, to create iterators, we can use both regular functions and generators. Generators are written just like a normal function but we use yield() instead of return() for returning a resul

"""


# Python code to illustrate generator, yield() and next().
def generator():
    t = 1
    print('First result is ', t)
    yield t

    t += 1
    print('Second result is ', t)
    yield t

    t += 1
    print('Third result is ', t)
    yield t


call = generator()
next(call)
next(call)
next(call)

# First result is  1
# Second result is  2
# Third result is  3

"""
Difference between Generator function and Normal function -

Once the function yields, the function is paused and the control is transferred to the caller.
When the function terminates, StopIteration is raised automatically on further calls.
Local variables and their states are remembered between successive calls.
The generator function contains one or more yield statements instead of a return statement.
As the methods like _next_() and _iter_() are implemented automatically, we can iterate through the items using next().

"""

# Python code to illustrate generator expression
generator = (num ** 2 for num in range(10))
for num in generator:
    print(num)

# 0 1 4 9 16 25 36 49 64 81

string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)

# ['k', 'e', 'e', 'g']
