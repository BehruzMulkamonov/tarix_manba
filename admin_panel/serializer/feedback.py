from rest_framework import serializers
from other_app.models import Feedbacks

class FeedbacksAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ['id', 'message', 'created_time', 'updated_time']


class FeedbacksAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ['message_en', 'message_ru', 'message_uz','created_time', 'updated_time']