from rest_framework import serializers
from .models import Book
from slots.serializers import SlotSerializer


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = '__all__'