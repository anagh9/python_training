# Class Based APIView
"""
Rest framework provides an APIView class, which subclasses Django's View class.
APIView classes are diffrent from reqular View classes in the following ways:-

- Requests passed to the handler methods will be RESST framework's Request instances,not Django's HttpRequest instances.

- Handler methods may return REST framework's Response , instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the resposne.

- Any APIException exceptions will be caught and meditated into appropriate responses.

- Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.

ex:-
""" 
from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        pass 
    def post(self,request,format=None):
        pass
    def put(self,request,pk,format=None):
        pass
    def patch(self,request,pk,format=None):
        pass
    def delete(self,request,pk,format=None):
        pass

    #same as function view