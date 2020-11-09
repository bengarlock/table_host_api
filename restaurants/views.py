from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Restaurant


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()