# Show Table Data to User

# all() - It returns a copy of current QuerySet or QuerySet subclass .
"""
Syntax :-
ModelClassName.objects.all()

"""

from enroll.models import Student


def studentinfo(request):
    stud = Students.objects.all()
    return render(request, 'enroll/studeetails.html', {'stu': stu})


"""

{% if stu %}
  <h1>Show Data </h1>
  {% for item in stu %}
        {{item.stuname}}
        {{item.id}}
  {% endfor %}
{% else %}
    <h1>No data</h1>
{% endif %}
"""

# How to register model

# Open admin.py in application folder
# Import your own Model class created inside application's models.py
# admin.site.register(ModelClassName)

"""
The __str__() method is callled whenerver you call str() on an object . To display an object in the django admin site and as the value inserted into a template when it displays an object. Thus, you should always return a nice, human readable representation of the model from __str__() method.
"""


def __str__(self):
    return self.stuname
