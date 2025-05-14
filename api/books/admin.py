from django.contrib import admin

from api.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'published', 'pages', 'created_at')
    list_filter = ('author', 'published')
    search_fields = ('isbn', 'title', 'author')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

