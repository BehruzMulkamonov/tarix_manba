from rest_framework import serializers
from other_app.models import Sliders

class SlidersAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = ['id','title', 'file', 'link', 'created_time', 'updated_time']


class SlidersAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = ['title_en', 'title_ru', 'title_uz', 'file', 'link', 'created_time', 'updated_time']