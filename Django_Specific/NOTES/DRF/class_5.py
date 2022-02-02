# Validation 

# - Field Level Validation 
# - Object Level Validation
# - Validators 


# - Field Level Validation 
"""
We can specify custom field-level validaition by adding validate fieldName methods to your Serializer subclass

These are similar to the clean_fieldName methods on Django Forms

validate_fieldName methods should return the validated value or raise a serializers.ValidationError

Syntax:-
def validate_fieldName(self,value):
    pass

ex:-
def validate_roll(self,value):
    pass

value is the field that requires validation
ex:-
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')


"""

# Object level validation:

"""
When w need to do validation that requires access to multiple fields we do object level vaidation by adding a method called validate() to Serializer subclass

It raises a serializers.ValidationError if neccessary, or just retuen the validated values.

Syntax:- def validate(self,data)
Example :- def validate(self,data)
Where data is a dictionary of field values


ex:-
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower!='ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data



"""

# - Validators 

"""
Most of the time youre dealing with validation in REST framework youwill simly be reluing on the efault field validation, or writing explicit validation methods on serializer or field classes.

However, sometimes you'll want to place your validation logic into reusable components, so that it can easily be reused throughout your codebase. This can be achieved by using validator functions and validator classes 

- It introduces a proper seperation of concerns , making your code behaviour more obvious.

- It is easy to switch between using shortcut ModelSerializer classes and using explicit Serializer classes. Any Validation behaviour being used for ModelSerializer is simple to replicate.

- Printing the repr() of a serializer instance will show yo exactly what validation rules it applies. There's no extra hidden validation behaviour being called on the model instance.

- When you're using ModelSerializer all of this is handled automatically for you. If you want tp drop down to using Serializer classes instead, then you need to define the validation rules explicitly.


from rest_framework import serializers
def starts_with_r(value):
    if value['0'].lower()!='r':
        raise serializers.ValidationError('Name should start with R')
    
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

For Multiple validator function seperate it with comma.

Priority:
1. Validators
2. Field level Validators
3. Object level validators
"""

