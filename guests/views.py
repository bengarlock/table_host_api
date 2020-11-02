from typing import List

from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Guest
from .serializers import GuestSerializer


class GuestView(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = ["first_name", "last_name", "phone_number"]

#http://127.0.0.1:8000/guests/?search=mcdaniel