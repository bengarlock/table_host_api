from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
import django_filters.rest_framework


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['date']


