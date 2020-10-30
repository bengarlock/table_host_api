from rest_framework import serializers
from .models import Slot
from guests.serializers import GuestSerializer

class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = '__all__'

    def create(self, validated_data):
        return Slot(**validated_data)

    def update(self, instance, validated_data):
        print(instance)
        instance.booked = validated_data.get('booked', instance.booked)
        return instance



