from django.shortcuts import render
from rest_framework import viewsets
from .models import Guest
from .serializers import GuestSerializer
import django_filters.rest_framework

class GuestView(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    filterset_fields = ["first_name"]
