# Form Field
# A form field are themselves classes they manage form data and perform validation when a form is submitted
"""
Syntax :- FieldType(** kwargs)
Example :-
IntegerField()
CharField(required)
CharField(required,widget='Textarea')

from djanog import forms 
class StudentRegistration(forms.Form):
    name = forms.CharField()
"""

# Field Arguments
"""
required
label
label_suffix
initial - initial value to input field
disabled - True/False
help_text - use as help in span below input
error_messages
validators
localize 
widget
"""

from django import forms 
class StudentRegistration(forms.Form):
    name = forms.CharField(label = 'Your Name',label_suffix = ' ', initial='Soname',required=False,disabled=True,help_text='Limit 70 Char')
