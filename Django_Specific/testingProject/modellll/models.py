from django.db import models
from django.db.models.base import Model
from datetime import date
# Create your models here.
def age_check(value):
    if value > 150:
        return False
    else:
        return True


class Home(models.Model):
    name = models.CharField(max_length=320)
    age = models.PositiveIntegerField(validators=[age_check],default=0)
    is_active = models.BooleanField(default=False)




class DateVisit(models.Model):
    datee = models.DateField(default=date.today)

class X(Home):
    class Meta:
        proxy = True