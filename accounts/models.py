from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
)
from .manager import MyUserManager



class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email' # user authentication
    REQUIRED_FIELD = ['phone'] # ask when create super user in command line


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): # is user has special permissions?
        return True

    def has_module_perms(self, app_label): # is user has module app permissions
        return True

    @property
    def is_staff(self): # permissions to access Admin Panel
        return self.is_admin