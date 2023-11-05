from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.users.manager import UserManager

# Create your models here.
class UsersModel(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    def __str__(self):
        return self.email