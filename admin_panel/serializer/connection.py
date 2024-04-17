from rest_framework import serializers
from other_app.models import Connection

class ConnectionAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'phone', 'phone_two', 'address', 'location', 'email', 'map', 'created_time', 'updated_time']

class ConnectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['phone', 'phone_two', 'address_en', 'address_ru', 'address_uz', 'location_en', 'location_ru', 'location_uz', 'email', 'map_en', 'map_ru', 'map_uz', 'created_time', 'updated_time']