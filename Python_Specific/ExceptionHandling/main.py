"""
# https://www.tutorialsteacher.com/python/error-types-in-python
Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

"""

a = [1, 2, 3]
try:
    print(f'Second element is {a[1]}')
    print(f'Fourth element is {a[3]}')
except:
    print('An error occurred')


# Catching Specific Exception
"""
try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
"""

try:
    a = 5
    b = '0'
    print(a+b)
except TypeError:
    print('Unsupported operation')
print("Out of try except blocks")


try:
    a = 5
    b = 0
    print(a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero not allowed')
print('Out of try except blocks')
