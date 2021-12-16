def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("Display function ran")


decorated_display = decorator_function(display)
decorated_display()

# We can simplify using below code


@decorator_function
def display():
    print('display function ran')


display()

# line 19 is same as line 11 and 12

decorated_display = decorator_function(display)
# is same if we declare @decorator_function above display
# it's equivalent to display()
