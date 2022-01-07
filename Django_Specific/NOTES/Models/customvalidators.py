# field_name = models.Field(validators = [function 1, function 2]) 

from django.db import models
# importing validationerror
from django.core.exceptions import ValidationError

# creating a validator function
def validate_geeks_mail(value):
	if "@gmail.com" in value:
		return value
	else:
		raise ValidationError("This field accepts mail id of google only")


# Create your models here.
class GeeksModel(models.Model):
	geeks_mail = models.CharField(
						max_length = 200,
						validators =[validate_geeks_mail]
						)


"""
Basic model data types and fields list
The most important part of a model and the only required part of a model is the list of database fields it defines. Fields are specified by class attributes. Here is a list of all Field types used in Django.

Field Name	Description
AutoField	It An IntegerField that automatically increments.
BigAutoField	It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.
BigIntegerField	It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
BinaryField	A field to store raw binary data.
BooleanField	A true/false field.
The default form widget for this field is a CheckboxInput.
CharField	It is a date, represented in Python by a datetime.date instance.
DateField	A date, represented in Python by a datetime.date instance
It is used for date and time, represented in Python by a datetime.datetime instance.
DecimalField	It is a fixed-precision decimal number, represented in Python by a Decimal instance.
DurationField	A field for storing periods of time.
EmailField	It is a CharField that checks that the value is a valid email address.
FileField	It is a file-upload field.
FloatField	It is a floating-point number represented in Python by a float instance.
ImageField	It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
IntegerField	It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
GenericIPAddressField	An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).
NullBooleanField	Like a BooleanField, but allows NULL as one of the options.
PositiveIntegerField	Like an IntegerField, but must be either positive or zero (0).
PositiveSmallIntegerField	Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point.
SlugField	Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
SmallIntegerField	It is like an IntegerField, but only allows values under a certain (database-dependent) point.
TextField	A large text field. The default form widget for this field is a Textarea.
TimeField	A time, represented in Python by a datetime.time instance.
URLField	A CharField for a URL, validated by URLValidator.
UUIDField	A field for storing universally unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32).

"""