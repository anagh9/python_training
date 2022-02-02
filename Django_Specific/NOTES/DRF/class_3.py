# Serializer Class
"""
Serializer fields handle converting beteween primitive values and internal datatypes. They also deal with validating input values , as well as retrieving and setting the values from their parent objects.

Syntax:-
from rest_framework import serializers
serializers.FieldName()

ex:-
CharField
IntegerField
SlugField
ImageField
JSONField
"""

# DeSerialization
import json
import requests
deserialization_defination = "Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex types , after first validating the incoming data. "

# JsonData =(Parse Data)=> PythonNativeDataType =(DeSerialization)=> ComplexDatatype

# Notes
"""
- BytesIO() - A stream implementation using an in-memory bytes buffer. It inherits BufferIOBase. The Buffer is discarded when the close() method is called
ex :-
import io
stream = io.BytesIO(json_data)

- JSONParser()
This is used to parse json data to python native data type.
ex:-
from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)

- De-Serialization
 De-Serialization allows parsed data to be converted back into complex types, after validating the incoming data.

 ex-:
- Creating Serializer Object
serializer = StudentSerializer(data = parsed_data)

- Validated Data 
serializer.is_valid()

if valid then use (serializer.validated_data)
else (serializer.errors)

Use use Deserialization for converting json data into models table.
"""
"""
Ex:-
Create Data/Insert Data
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = seializers,IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)


--Changed In Views
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import jsonRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def nameofviews(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
    
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            retun HttpResponse(json_data,content_type="application/json") 
        
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json") 

"""

# Post method from python file
URL = ""
data = {
    "name": "Soname",
    "roll": 101,
    "city": "Ranchi"
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)

data = r.json
print(data)
