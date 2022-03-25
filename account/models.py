from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Почта обязательна")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
