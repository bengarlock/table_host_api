from rest_framework import serializers
from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

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
