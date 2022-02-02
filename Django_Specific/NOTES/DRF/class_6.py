# ModelSerializer Class 

"""
The ModelSerializer class provides a shortcut that lets you automatically create a Serualizer class with fields that correspond to the Model fields.

The ModelSerializer class is the same as a regular Serializer class, expect that:
- It will automatically generate a set of fields for you, based on the model.
- It will automatically generate validators for the serializer , such as unique_together validators.
- IT includes simple default implementation of create and update().
"""

# Create ModelSerializer class
# serializers.py
"""
example:-

from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = ['id','name','roll','city']

- fields = "__all__"
- exclude =['roll']


for making anything not to change 
class StudentSerializer(serializers.ModelSerializer):
    # For single field
    name = serializers.CharField(read_only = True)
    class Meta:
        model =Student
        fields = ['id','name','roll','city']
        # for multiple read_only fields
        read_only_fields = ['name','roll']

        # or 
        extra_kwargs = {'name':{'read_only':True}}

"""