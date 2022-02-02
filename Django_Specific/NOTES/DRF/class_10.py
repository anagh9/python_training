# Concrete View Class

"""
The following classes are the concrete generic views

If you're using generic views this is normally the level you'll be working at unless you need heavily customized behaviour.

The view classes can be imported from rest_framewok.generics.

- ListAPIView - It is used for read only endpoints to represent a collection of model instances. It provides a get method handler.

Extends :- GenericAPIView, LitModelMixin
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- CreateAPIView -  It is used for create-only endpoints. It provides a post method handler.

Extends :- GenericAPIView, CreateModelMixin
from rest_framework.generics import ListAPIView
class StudentList(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


- RetrieveAPIView - It is used for read-only endpoints to represent a single model instance. It provides a get method handler.

Extends :- GenericAPIView, RetrieveModelMixin
from rest_framework.generics import RetrieveAPIView
class StudentList(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


- UpdateAPIView - It is used for update-only endpoints for a single model instance. It provides put and patch method handlers.

Extends:- GenericAPIView, UpdateModelMixin
from rest_framework.generics import UpdateAPIView
class StudentList(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- DestroyAPIView - It is used for delete-only endpoints for a single model instance. It provides a delete method handler.

Extends:- GenericAPIView, DestroyModelMixin
from rest_framework.generics import DestroyAPIView
class StudentList(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- ListCreateAPIView - It is used for read-write endpoints to represent a collection of model instances. It provides get and post method handlers.

Extends:- GenericAPIView, ListModelMixin,CreateModelMixin
from rest_framework.generics import ListCreateAPIView
class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- RetrieveUpdasteAPIView - It is used for read or update endpoints to represent a single model instance. It provides get, put and patch method handlers.

Extends:- GenericAPIView, RetrieveModelMixin,UpdateModelMixin

from rest_framework.generics import RetrieveUpdateAPIView
class StudentCreate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- RetrieveDestroyView - It is used for erad or delete endpoints to represent a single model instance. It provides get and delete method handlers.

Extends:- GenericAPIView, RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import RetrieveUpdateAPIView
class StudentRetrieve(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

- RetrieveUpdateDestroyAPIView -It is used fro read-write-delete endpoints to represent a single model instance. It provides get,put,patch and delete method handlers.

Extends:- GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework.generics import RetrieveUpdateDestroyAPIView
class StudentUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


url - path('studentapi/<int:pk>/',views.StudentRetrieve.as_view())
"""


# CRUD


from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView

class StudentList(ListAPIView):
    queryset = Student.object.all()
    serializer_class = StudentSerializer

# path('api/',views.StudentList.as_view())

class StudentList(CreateAPIView):
    queryset = Student.object.all()
    serializer_class = StudentSerializer


