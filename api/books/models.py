# models.py
from django.db import models

from api.base.mixins import TimeModelMixin


# models.py
class Book(TimeModelMixin):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    cover = models.URLField(null=True, blank=True)
    author = models.CharField(max_length=255)
    published = models.IntegerField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=2)

    class Meta:
        db_table = 'books'
