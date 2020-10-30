from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.class_name = validated_data.get('class_name', instance.class_name)
            instance.position_left = validated_data.get('position_left', instance.position_left)
            instance.position_top = validated_data.get('position_top', instance.position_top)
            instance.name = validated_data.get('name', instance.name)
            instance.restaurant_id = validated_data.get('restaurant_id', instance.restaurant_id)
            instance.status = validated_data.get('status', instance.status)
            instance.save()