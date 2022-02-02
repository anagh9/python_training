# Token Authentication 
"""
This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.

To use the TokenAuthentication scheme you'll need to configure the authentication classes to include TokenAuthentication, and additionally include rest_framework.authtoken in your INSTALLED_APPS setting:
"""

INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken'
]

# Note: Make sure to run manage.py migrate after changing your settings. The rest_framework.authtoken app provides Django database migrations.

"""
Note: If you want to use a different keyword in the header, such as Bearer, simply subclass TokenAuthentication and set the keyword class variable.

If successfully authenticated, TokenAuthentication provides the following credentials.

request.user will be a Django User instance.
request.auth will be a rest_framework.authtoken.models.Token instance.
Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header
"""
# Generate Token 

# python manage.py drf_create_token <username> - This command will return API Token for the given user or creates a token if token does'nt exist for user 

# - By exposing an API endpoint 
# - In urls.py 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('gettoken/',obtain_auth_token)
]

# The obtain_auth_token view will return a JSON response when valid username and password fields are POSTED to the view using form data or JSON :

# pip install httpie 

# http POST http://127.0.0.1:8000/gettoken/username="name" password="pass"

