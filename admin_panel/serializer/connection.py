from rest_framework import serializers
from other_app.models import Connection

class ConnectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'
