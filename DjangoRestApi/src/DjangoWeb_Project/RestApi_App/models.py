from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManger(BaseUserManager):
    """ Help django to work with our custome models """

    #function to create users
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User must have an email address')

        email.sel.normalize_email(email)
        user = self.model(email=email, name= get_full_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    #function to create Super users or admin
    def create_superuser(self,email,name,password):
        """ create and save new super user """
        user = self.create_user(email,name,password)
        user.is_Superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return  user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Represents a user profile in or system """
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_Staffctive = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    #Object Manager to have a customized manager than th eprovided default
    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a userd full name"""
        return self.name

    def get_short_name(self):
        """Used to get a userd short/first/nick name"""
        return self.name
    def _str_(self):
        """Used by django to convert objects to string"""
        return self.email
