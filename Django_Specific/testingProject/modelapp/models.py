from django.db import models
import datetime
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField, create_many_to_many_intermediary_model

# Create your models here.


class CustomManger(models.Manager):
    def saurabh(self):
        print("Hello It's Working")
        return None


class School(models.Model):
    school_id = models.IntegerField(primary_key=True)
    school_title = models.CharField(max_length=50)
    level_count = models.SmallIntegerField(null=True)
    is_active = models.SmallIntegerField(default=False)
    created_At = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(null=True)


class Student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True)
    student_code = models.CharField(max_length=12, null=False)
    full_name = models.CharField(max_length=50, null=True)
    gender = models.SmallIntegerField()
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    school_id = models.ForeignKey(School, on_delete=CASCADE)
    stage = models.IntegerField()
    section = models.CharField(max_length=2)
    is_active = models.SmallIntegerField(default=False)
    join_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    items = models.Manager()
    sort = CustomManger()


class Parent(models.Model):
    student_parent = models.ManyToManyField(Student)
    parent_id = models.IntegerField(primary_key=True)
    parent_code = models.CharField(max_length=12, null=True)
    parent_full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(null=True)


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_code = models.CharField(max_length=12)
    teacher_full_name = models.CharField(max_length=75)
    gender = models.SmallIntegerField()
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_active = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class classroom(models.Model):
    classroom_id = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    room_type = models.IntegerField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    school_id = ForeignKey(School, on_delete=CASCADE)
    stage = models.IntegerField()
    team = models.IntegerField()
    carry_mark = IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Class(models.Model):
    class_student = models.ManyToManyField(Student)
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=50)
    subject_id = ForeignKey(Subject, on_delete=CASCADE)
    teacher_id = ForeignKey(Teacher, on_delete=CASCADE)
    classroom_id = ForeignKey(classroom, on_delete=CASCADE)
    section = models.CharField(max_length=12)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Fake(models.Model):
    fakename = models.CharField(max_length=100)


class DeepFake(models.Model):
    deep = OneToOneField(Fake, on_delete=CASCADE)
