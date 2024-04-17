from rest_framework import serializers
from other_app.models import Comments

class CommentsAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'message', 'created_time', 'updated_time']


class CommentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['message_ru', 'message_ru', 'message_uz',  'created_time', 'updated_time']
