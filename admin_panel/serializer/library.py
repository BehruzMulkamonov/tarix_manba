from rest_framework import serializers
from other_app.models import Library

class LibraryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
