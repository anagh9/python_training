"""
Q> When To use middleware ?

- Filtering Requests
- Injecting Data into Requests/Response
- Performing Logging / Page Analytics 

Q> Types of middleware?

- Function Based middleware -> Takes a get_response callable and returns a middleware. A middleware is a callable that rakes a request and returns a response ,just like view.
"""


def my_middleware(get_response):
    # One-time configuration and initialization.
    def my_function(request):
        # Code to be executed for each request before the view are called.
        response = get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response
    return my_function


# - Class Based middleware


# user -> middleware -> server
# user <- middleware <- server

# get_response() - The get_response callable provided by Django might be the actual view (if this is the last listed middleware) or it might be the next middleware ) it might be the next middleware int the chain.

# Steps to write middleware
# To activate a middleware component ,add it to bhe MIDDLEWARE list in your Django settings.
# - Write Full path in settings.py MIDDLEWARE block.
MIDDLEWARE = [
    '.....',
    '.....',
    'appname.filename_name.function_name'
]
