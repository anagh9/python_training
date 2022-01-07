"""
AbstractUser class inherits the User class and is used to add Additional Fields required for your User in Database itself. SO its change the schema of the database. It is basically used to add fields like date_of_birth , location and bio etc. to the existing User model This is Done to the very Beginning of the project
"""

from django.contrib.auth import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth  = models.DateField()
    address = models.CharField(max_length=100,blank=True)
    bio_info = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.email

"""
AbstractBaseUser has the authentication functionality only , it has no actual fields you will supply the fields to use when you subclass.
you have to till that what field represent username fields, and how those users will be managed
for example you have to use email in your authentication , Normally Django use username in authentication, so how do you change it to use email?
"""

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name= 'email address',
        max_length = 255,
        unique = True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

"""
If you need full control over User model, it is better to use AbstractBaseUser but if you are just adding things to the existing user, for example, you just want to add an extra field bio ,location field or any other profile data then use AbstractUser.
"""