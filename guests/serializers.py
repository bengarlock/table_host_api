from rest_framework import serializers
from .models import Guest
from slots.models import Slot



class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'book']
        depth = 1

class GuestSerializer(serializers.ModelSerializer):

    # slot = SlotSerializer(many=True)

    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'guest_notes', 'root_user']

    def update(self, instance, validated_data):
        phone_number = instance.phone_number
        str(phone_number)
        bad_chars = [';', ':', '!', "*", ",", ".", "-", "+1"]

        for i in bad_chars:
            phone_number = phone_number.replace(i, '')

        validated_data["phone_number"] = phone_number


        if instance.root_user:
            pass
        else:
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.guest_notes = validated_data.get('guest_notes', instance.guest_notes)
            instance.save()

        return instance

