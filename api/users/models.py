from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from api.base import TimeModelMixin


class CustomUserManager(UserManager):
    def create_user(self, name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(name, email, password, **extra_fields)


class UserAuth(TimeModelMixin, AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'