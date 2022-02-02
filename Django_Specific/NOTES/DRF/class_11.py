# ViewSet 

"""
Django Rest Framework allows you to combine the logic for a set if related views in a single class called a ViewSet.

There are two main advantages of using a ViewSet over using a View class.

- Repeatedly logic can be combined into a single class.
- By using routers, we no longer need to deal with wiring up the URL conf ourselves.
"""

# ViewSet Class 
"""
A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as get() or post() and instead provides actions such as list() and create().

- list() - Get All Records
- retrieve() - Get Single Record
- create() - Create/Insert Record
- update() - Update Record Completely
- partial_update() - Update Record Partially
- destroy() - Delete Record 
ex:- 

from rest_frameworj import viewsets

class StudenViewSet(viewsets.ViewSet):
    def list(self,request): ...
    def create(self,request): ...
    def retrieve(Self,request,pk=None):...
    def update(self,request,pk=None):....
    def partial_update(self,request,pk=None):...
    def destroy(self,request,pk=None):...

During dispatch , the following attributes are available on the ViewSet:-

- basename - the base to use for the URL names that are created.

- action - the name of the current actions(eg:- list,create)

- detail - boolean indicating if the current action is configured for a list or detail view.

- suffix - the display suffix for the viewset type  mirrors the detail attribute.

- name - the display name for the viewset . Thos argument is mutuallly exclusive to suffix.

- description - teh display description for the individual vie of a viewset

ViewSet - URL Config
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path(",",include(routers.urls))
]

"""