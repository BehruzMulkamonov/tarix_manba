from rest_framework import serializers
from other_app.models import Connection

class ConnectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'phone', 'phone_two', 'address', 'location', 'email', 'map', 'created_time', 'updated_time']
