from rest_framework import serializers
from other_app.models import Library

class LibraryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','title', 'category','author', 'type', 'year', 'country', 'language', 'image', 'file',  'created_time', 'updated_time']