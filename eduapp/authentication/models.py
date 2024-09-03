
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

ROLES = [
    ('admin', 'Admin'),
    ('user', 'User')
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, fullname, role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, role='admin', **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, fullname, password, role, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(choices=ROLES, default='user', max_length=10)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'role']

    def __str__(self):
        return self.email