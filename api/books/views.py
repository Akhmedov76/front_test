from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.base.openlibrary import get_book_data_by_isbn
from api.books.models import Book
from api.books.serializers import BookSerializer


class BookViewSet(viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BookSerializer)
    @action(detail=False, methods=['POST'])
    def create_books(self, request):
        isbn = request.data.get('isbn')
        book_data = get_book_data_by_isbn(isbn)

        if not book_data:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        book_data['created_by'] = request.user.id

        serializer = self.get_serializer(data=book_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'], url_path='(?P<title>.*)')
    def search_by_title(self, request, title=None):
        key = request.headers.get('Key')
        sign = request.headers.get('Sign')

        if not key or not sign:
            return Response(
                {"error": "Key and Sign headers are required"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not title:
            return Response(
                {"error": "Title parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        books = Book.objects.filter(title__icontains=title)
        if not books.exists():
            return Response(
                {"error": "No books found with this title"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_all_books(self, request):
        key = request.headers.get('Key')
        sign = request.headers.get('Sign')

        if not key or not sign:
            return Response(
                {"error": "Key and Sign headers are required"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
