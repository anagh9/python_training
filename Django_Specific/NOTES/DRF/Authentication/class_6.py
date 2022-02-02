# JSON WEB TOKEN .

# JSON web token is a fairly new standard which can be used for token based authentication. Unlike the builtin TokenAuthentication scheme, JWT authentication doesn't need to use a database to validate a token.

# https://jwt.io/
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest

# pip install djangorestframework-simplejwt

# Configure simple jwt
# - settings.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.simplejwt.authentication import JWTAuthentication
from datetime import timedelta
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAUthentication',
    )
}

# urls.py

urlpatters = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify')
]

# In setting.py

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SINGNING_KEY': settings.SECRET_KEY,

}

# tHEN In Views.py


authentication_classes = [JWTAuthentication]
permission_classes = [IsAuthenticated]
