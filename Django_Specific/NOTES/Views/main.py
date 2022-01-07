# Class-based views - A view is a callable which takes a request and returns a response.

"""
At its core, a class-based view allows you to respond to different HTTP request methods with different class instance methods, instead of with conditionally branching code inside a single view function.
So where the code to handle HTTP GET in a view function would look something like:
"""

from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')


# In a class-based view, this would become:

from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

from django.urls import path
urlpatterns = [
    path('about/', MyView.as_view()),
]

