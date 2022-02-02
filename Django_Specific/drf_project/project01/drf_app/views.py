from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer
from .serializers import StudentSerializer
from .models import Student
import json
from .play import serializer


def index(request):
    stu = Student.objects.all()
    serialize = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serialize.data)
    print(serializer.data)
    jso = JSONRenderer().render(serializer.data)
    return HttpResponse(jso, content_type='application/json')


def singleindex(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# def test_main(reuest):
#     obj = json.dumps({"success": True})
#     return HttpResponse(obj, content_type='application/json')
