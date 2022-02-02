from django.db.models import fields
from rest_framework import serializers
from .models import Student
import datetime
class StudentSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(default=datetime.datetime.now())
    manager = serializers.CharField(default="ANAGH KUMAR")
    class Meta:
        model = Student
        fields = ['id','name','branch','is_active','time','manager']
        # fields = "__all__"