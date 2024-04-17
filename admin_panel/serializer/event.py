from rest_framework import serializers
from other_app.models import Event

class EventAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'content', 'image', 'created_time', 'updated_time']


class EventAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title_en', 'title_ru', 'title_uz', 'content_en', 'content_ru', 'content_uz', 'image', 'created_time', 'updated_time']