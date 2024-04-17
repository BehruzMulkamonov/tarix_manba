from rest_framework import serializers
from other_app.models import News

class NewsAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title', 'content', 'file',  'created_time', 'updated_time']

class NewsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title_en', 'title_ru', 'title_uz', 'content_en', 'content_ru', 'content_uz', 'file',  'created_time', 'updated_time']