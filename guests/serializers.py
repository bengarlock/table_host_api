from rest_framework import serializers
from .models import Guest
from slots.serializers import SlotSerializer

class GuestSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)

    class Meta:
        model = Guest
        fields = '__all__'
