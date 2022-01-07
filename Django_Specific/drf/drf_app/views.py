from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student
from drf_app import serializers
# Create your views here.


def index(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def singleindex(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
