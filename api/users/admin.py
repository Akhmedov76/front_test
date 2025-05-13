from django.contrib import admin
from django.contrib.auth.models import Group

from .models import UserAuth


@admin.register(UserAuth)
class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'key', 'secret')
    search_fields = ('name', 'email', 'key')
    list_filter = ('key',)


admin.site.unregister(Group)
