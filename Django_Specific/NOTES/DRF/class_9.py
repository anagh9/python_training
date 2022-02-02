# Generic APIView 

"""
This class extends REST framework's API View class, adding commonly required behaviour for standard list and detail views

- Attributes
queryset - THE queryset that should be used for returning objects from this view. Typically, you must either set this attribute, or override the get_queryset() method. If you are oveririding a view method, it is important that you call get_queryset() instead of accesing this property directly, as queryset will get evaluated once, and those results will be cached for all subsequent requests.

- serializer_class - The serializer class that should be used for validating and deserialising input, and for serializing output . Typically, you must either set this attribute , or override the get_serializer_class() method.

- lookup_field - The model field that should be used to for performing object lookup of individual model istances

- lookup_url_kwarg
- pagination_class
- filter_backends

## Methods
- get_queryset(self) => For customizing code and rendering the part which we want.
- get_object(self)
- get_serializer_class(self)
- get_serializer_context(self)
- get_serializer(self,instance=None,many=False,partial=False)
- get_paginated_response(self)
- field_queryset(self,request)
"""

###########################################
# Mixins

"""
The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior.

The mixin classes can be imported from rest_framework.mixins.

The mixin classes provide the actions that are used to provide the basic view behaviour.

- ListModelMixin - It provides a list(request.*args,**kwargs) method, that implements listing a queryset.

If the queryset is populated , this returns a 200 OK response, with a serialized representation of the queryset as the body of the response . The response data may optionally be paginated.

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(ListModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


- CreateModelMixin -  It provide a create(request.*args,**kwargs) method, that implements creating and saving a new model instance.

If an object is created this returns a 201 Created response, with a serialized representation of the object as the body of the response . If the representation contains a key named url,then the location header of the response will be populated with that value

If the request data provided for creating the object was invalid, a 400 Bad Request resonse will be returned, with the error details as the body of the response.

from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(CreateModelView,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


- RetrieveModelMixin -  It provide a retrieve(request.*args,**kwargs) method, that implements returning an existing model instance in a response.

If an object can be retrieved this returns a 200 OK response, with a serialized representation of the object as the body of the reponse . Otherwise it will return 404 Not Found.

from rest_framework.mixins import RetriveModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(RetriveModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

- UpdateModelMixin - It provide a update(request.*args,**kwargs) method, that implements updating and saving an existing model instance in a response

It also provides a partial_update(request, *args,**kwargs) method which is similar to the update method , except that all fields for the update will be optional. This allows support for HTTP PATCH request.

If an object is updated this returns a 200 OK response, with a serialized representation of the object as the body of the response.

If data invalid we get errors with status code 400

from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(UpdateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

- DestroyModelMixin - It provide a destroy(request.*args,**kwargs) method, that implements deletion of an existing model instance 

If an object is eleted thid response status as 204

from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import GenericAPIView

class StudentList(DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

"""
### CRUD Operations.
# models 
# serilizers 
# In views 

# GenericAPIView and Model Mixin
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, ListModelMixin,CreateModelMixin, RetriveModelMixin, UpdateModelMixin

# List and Create are of same group 
# Retrieve , Update and Destroy are of Same Group. 

class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

# url - StudenList.as_view()

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# url - StudentCreate.as_view()

class StudentRetrive(GenericAPIView,RetriveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

# url - StudentRetrive.as_view()

# Same for Update And Delete  


# Common For All Generic CRUD

class LC_StudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)    

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# path('api/',views.LC_StudentAPI.as_view())

# Retrieve_update_delete
class RUD_StudentAPI(GenericAPIView,RetriveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)    

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# path('api/<int:pk>',views.LC_StudentAPI.as_view())

