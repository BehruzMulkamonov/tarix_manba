from rest_framework import serializers
from other_app.models import Event

class EventAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
