from rest_framework import serializers, fields
from .models import Slot
from .models import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'guest_notes', 'root_user']


class SlotSerializer(serializers.ModelSerializer):
    guest = serializers.SerializerMethodField('get_guest_data')

    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'book', 'guest']

    def get_guest_data(self, slot):
        print(slot)
        guest = {
            "id": slot.guest.id,
            "first_name": slot.guest.first_name,
            "last_name": slot.guest.last_name,
            "phone_number": slot.guest.phone_number,
            "guest_notes": slot.guest.guest_notes,
            "root_user": slot.guest.root_user,
        }

        return guest

    def create(self, validated_data):
        Slot.objects.create(**validated_data)
        return Slot(**validated_data)

    def update(self, instance, validated_data):
        guest_data = validated_data.pop('guest')
        print(validated_data)

        instance.booked = validated_data.get('booked', instance.booked)
        instance.time = validated_data.get('time', instance.time)
        instance.party_size = validated_data.get('party_size', instance.party_size)
        instance.status = validated_data.get('status', instance.status)
        instance.reservation_notes = validated_data.get('reservation_notes', instance.reservation_notes)
        instance.tables = validated_data.get('tables', instance.tables)
        instance.save()


        #
        # for item in guest_data:
        #      item.first_name = guest_data.get('first_name', item.first_name)
        #      item.last_name = guest_data.get('last_name', item.last_name)
        #      item.phone_number = guest_data.get('phone_number', item.phone_number)
        #      item.guest_notes = guest_data.get('guest_notes', item.guest_notes)
        #      item.root_user = guest_data.get('root_user', item.root_user)
        #      item.save()

        return instance
