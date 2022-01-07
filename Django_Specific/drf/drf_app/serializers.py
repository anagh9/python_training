from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=52)
    branch = serializers.CharField(max_length=20)
    is_active = serializers.BooleanField()