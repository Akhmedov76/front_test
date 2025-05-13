from django.contrib.auth.models import AbstractUser
from django.db import models

from api.base import TimeModelMixin


class UserAuth(TimeModelMixin, AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        self.username = self.name

