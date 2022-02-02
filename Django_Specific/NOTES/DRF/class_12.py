# - Model ViewSet 
"""
Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.
"""


from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets 

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
