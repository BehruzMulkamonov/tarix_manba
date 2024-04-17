from rest_framework import serializers
from other_app.models import Library_Category

class Library_CategoryAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Library_Category
        fields = ['id','title', 'created_time', 'updated_time']

class Library_CategoryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Category
        fields = ['title_en', 'title_ru', 'title_uz', 'created_time', 'updated_time']