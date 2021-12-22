# Django Form - Djano's  form functionality can simplify and automate vast portions
# of work like data prepared fordisplay in aform rendered as HTML, edit using a convinient interface

"""
It Handles three distinct parts of the work involved in forms
- preparing and restructuring data to make it ready for rendering
- creating HTMl forms for the data
- recieving and processing submitted forms and data from the client
"""

# Create Django Form Using Form Class
"""
To create Django form we have to create a new file inside application folder lets say file name is forms.py . Now we can write below code inside forms.py to create a form :-

Syntax :-
from django import forms
class FormClassName(forms.Form):
    label = forms.FieldType()
    label = forms.FieldType(label='display_label')


Example :-
form django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField() - Text
    email = forms.EmailField() - Email 
    form.IntegerField() - Number
 
"""


"""
### Display Form to user
Creating an object of Form class in views.py then pass object to template files
Use Form object in template file

# Creating Form object in views.py 
First of all create form object inside views.py file then pass this object to template file as a dict

-- views.py
from .forms import StudentRegistration
def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})


-- In templates/enroll/userregistration.html
<body>
<form action="" method ="get">
    {{ form }} 
     or
     {{ form.as_table }}
     {{ form.as_p }}
     {{ form.as_ul }}
     {{ form.name_of_field }}
</form>
</body>
"""
