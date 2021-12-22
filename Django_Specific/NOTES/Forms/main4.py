# How to send GET Request
"""
Open browser and write url hit enter this is by default get request
Anchor Tag 
Form tag contains methods = 'GET'
Form tag with specifying method is by default GET 
"""

# - forms.py
from .forms import StudentRegistration
from os import name
from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


# Get Submitted Data in views.py
# views.py


def showformdata(request):
    if request.method = 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:', fm.cleaned_data['name'])
            print('email:', fm.cleaned_data['email'])
    else:
        fm = StudentRegistration()
    return render(request, enroll/userregistration.html, {'form': fm})


# return HttpResponseRedirect('/con/success/')
