from rest_framework import serializers
from .models import Slot
from guests.serializers import GuestSerializer

class SlotSerializer(serializers.ModelSerializer):

    guest = GuestSerializer()

    class Meta:
        model = Slot
        fields = '__all__'

    def create(self, validated_data):
        return Slot(**validated_data)

    def update(self, instance, validated_data):

        instance.booked = validated_data.get('booked', instance.booked)
        instance.time = validated_data.get('time', instance.time)
        instance.party_size = validated_data.get('party_size', instance.party_size)
        instance.status = validated_data.get('status', instance.status)
        instance.reservation_notes = validated_data.get('reservation_notes', instance.reservation_notes)
        instance.tables = validated_data.get('tables', instance.tables)
        guest = validated_data.get('guest')

        for item in guest:
            pass

        return instance



