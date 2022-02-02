# Custom Permissions 

# To implement a custom permission , override BasePermisison and implement either , or both of the following methods. 
"""
- has_permission(self,request,view)
- has_object_permission(self,request,view,obj)

the methods should return True if the request should be granted access , and False otherwise.
"""

# custompermissions.py 

class MyPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        return False 

# views.py
# import 
# ....
permission_classes = [MyPermission]
# ....

# Third party Packages 
"""
DRF - Access Policy 
Composed Permissions 
Rest Condition 
DRY Rest Permissions 
Django Rest Framework Roles 
Django Rest Framework API Key 
Django Rest Framework ROle Filters 
Django Rest Framework PSQ 
"""

