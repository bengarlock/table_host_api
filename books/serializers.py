from rest_framework import serializers
from .models import Book
from guests.models import Guest
from slots.models import Slot


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'book', 'guest']


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2