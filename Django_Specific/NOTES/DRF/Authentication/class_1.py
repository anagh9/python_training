

# Authentication - It is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with . The permission and throttling policies can then use those credentials to determine if the request should be permitted.

# Authetication is always run at the very start of the view ,before the permission and throttling checks occur, and before any other code is allowed to proceed.


# - Drf provides types of Authetication
"""
- Basic Authentication 
- Session Authentication 
- Token Authetication
- Remote User Authentication
- Custom Authentication
"""

#  Basic Authentication

"""
This authentication scheme uses HTTP Basic Authentication,signed agaist a user's username and password.

Basic authentication is generally only appropriate for testing.

If successfull authenticated,Basic Auhentication provides the following credentials.

- request.user will be a Django User instance
- request.auth will be None.


- If using in production you must ensure that your API is only available over https.
"""

"""
Permission

Permission are used ti grant or deny access for diffrent classes of users to diffrent parts of the API.

Permission checks are always run at the cery start of the view, before any other code is allowed to proceed.

Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted.

## Permission Classes
-- AllowAny
The allow any permission class will allow unrestricted access, regardlless of the request was authenticated or unauthenticated.

-- IsAuthenticated
The isauthenticated permission class will deny permission to any unauthenticated user,and allow permissio otherwise.

-- IsAdminUser
The isadminuser permission class will deny permission to any user, unless.is_staff is True in which case permisison will be allowed. THIS PERMISSION is suitable if you want your api to only be accessible to a subset of trusted administrators.

-- IsAuthenticatedOrReadOnly
-- DjangoModelPermissions
-- DjangoModelPermissionsOrAnonReadOnly
-- DjangoObjectPermissions
-- CustomPermissions
"""

# For Class Based API Implementation
# - BasicAuthentication
"""
- model 
- register to admin 
- serializer
- url 
- createsuperuser
"""




from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]


# Globally apply authentication
# In settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSRS': ['rest_framework.authentication.BasicAuthentication'],

    'DEFAULT_PERMISSION_CLASSRS': ['rest_framework.permissions.IsAuthenticated']
}
