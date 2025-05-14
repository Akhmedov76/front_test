from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(required=True)

    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'cover', 'author', 'published', 'pages']
        read_only_fields = ['id', 'created_at', 'updated_at']
