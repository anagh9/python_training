from django.db import models
import uuid

# Create your models here.


class Demo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    

    def __str__(self) -> str:
        return self.name


class Demo2(models.Model):
    name = models.CharField(max_length=20, editable=False, primary_key=True)
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.name
