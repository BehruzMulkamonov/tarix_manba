from rest_framework import serializers
from other_app.models import News

class NewsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title', 'content', 'file',  'created_time', 'updated_time']