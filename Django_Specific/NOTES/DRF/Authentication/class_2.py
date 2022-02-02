from telnetlib import AUTHENTICATION


# Session AUTHENTICATION 

"""
This authentication scheme uses Django's default session backend for authentication. Session authentication is appropriate for AJAX clients that are running in the same session context as your website.

If successfully authenticated, SessionAuthentication provides the following credentials.

request.user will be a Django User instance.
request.auth will be None.

Unauthenticated responses that are denied permission will result in an HTTP 403 Forbidden response.

If you're using an AJAX-style API with SessionAuthentication, you'll need to make sure you include a valid CSRF token for any "unsafe" HTTP method calls, such as PUT, PATCH, POST or DELETE requests. See the Django CSRF documentation for more details.

Warning: Always use Django's standard login view when creating login pages. This will ensure your login views are properly protected.

CSRF validation in REST framework works slightly differently from standard Django due to the need to support both session and non-session based authentication to the same views. This means that only authenticated requests require CSRF tokens, and anonymous requests may be sent without CSRF tokens. This behaviour is not suitable for login views, which should always have CSRF validation applied.

"""

from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

class StudenModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_class = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

# / - urls.py 
# path('auth/',include('rest_framework.urls',namespace='rest_framework'))

# Django Model permission 
"""
This permission class ties into Django's standard django.contrib.auth model permissions. Thos permission must only be applied to views that have a queryset properly set. Authorization will only be granted if the user is authenticated and has the relevent model permissions assigned.

- Post requests require the user to have the add permission on the model.

- PUT and PATCH requests require the user to have the change permisison on the model.

- Delete requests require the user to have the delete permission on the model.
"""

