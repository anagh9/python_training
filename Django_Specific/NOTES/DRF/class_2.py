# Serializers
"""
In Django REST Framework, serializers are responsible for converting complex data such as querysets and model instances to native Python datatypes (called serialization) that can then be easily rendered inot JSON,XML,or other content types which is understandable by FrontEnd.

Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex types, after first validating the incoming data.
"""

"""
A serializer class is very similar to Django Form and ModelForm class, and includes similar validation flags on the various fields, such as required,max_length and default.

DRF provides Serializers class which gives you a powerful , generic way to control the output of your responses , as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.
"""

# How to Create Serializer Class
"""
- Create a separete serializers.py file to write all serializers

ex -:

from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializer.CharField(max_length=100)
    roll = serializers.IntergerField()
    city = serializers.CharField(max_length=100)

"""

"""
Technical Understanding

- Write Model
- For converting models data in json format we need to write serializers 
- Every row in table is known as model object
- ComplexDatatype ==(serialization)=> Python Native Datatype ==(Render into Json)=> Json Data

The process of converting comples data such as querysets and modelinstances ti native Python datatypes are called as Serialization in DRF.

- Creating models Instance stu.
    stu = Students.objects.get(id=1)

- Converting model instance stu to Python Dict/Serializing Object.
    serializer = StudentSerializer(stu)

-- In case of queryset
- Creating Query set
    stu = Student.objects.all()

- Converting stu ti list of Python Dict/Serializing Query Set
    serializer =StudentSerializer(stu,many=True)

- If you want to see data of serializer
print(serializer.data)

"""


"""
JSON Renderer

This is used to render Serialized data into JSON which is understandable by FrontEnd.

# imporing JSONRenderer
from rest_framework.renderers import JSONRenderer

# Render the Data into JSON
json_data =JSONRenderer().render(serialized.data)

# Then return to the client
 return HttpResponse(json_data,content_type='spplication/json')
"""

"""
JSONResponse()

JsonResponse(data, encorder=DjangoJSONENcorder, safe=Ture, json_dumps_params=None,**kwargs)

An HttpResponse subclass that helps tocreate a JSON-encoded response. It inherits most behaviour from its superclass with a couple diffrences:

- It default Content-Type header is set to application/json

- The first parameter , data should be a dict instance. If the safe parameter is set to False it can be any JSON-Serialible object.

- The encorder,which defaults to django.core.serializers.json.DjangoJSONEncorder, will be used to serialize the data.

Shorthand instead of HttpResponse

return JsonResponse(serializer.data,safe = False)
"""
