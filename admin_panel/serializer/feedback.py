from rest_framework import serializers
from other_app.models import Feedbacks

class FeedbacksAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'
