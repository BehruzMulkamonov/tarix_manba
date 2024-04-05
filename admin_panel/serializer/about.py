from rest_framework import serializers
from other_app.models import About

class AboutAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        
