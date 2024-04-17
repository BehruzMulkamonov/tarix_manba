from rest_framework import serializers
from other_app.models import About


class AboutAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title_en', 'title_ru', 'title_uz', 'content_en', 'content_ru', 
                  'content_uz', 'created_time', 'updated_time')
        
        
class AboutAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'created_time', 'updated_time')