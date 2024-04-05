from rest_framework import serializers
from other_app.models import Comments

class CommentsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
