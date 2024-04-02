from rest_framework import serializers
from other_app.models import About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
