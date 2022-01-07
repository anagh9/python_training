from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=52)
    branch = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
