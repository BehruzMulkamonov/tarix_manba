from rest_framework import serializers
from other_app.models import Library

class LibraryAdminSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','title', 'category','author', 'type', 'year', 'country', 'language', 'image', 'file',  'created_time', 'updated_time']


class LibraryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['title_en', 'title_ru', 'title_uz', 'category','author_en', 'author_ru', 'author_uz', 'type_en', 'type_ru', 'type_uz', 'year', 'country_en', 'country_ru', 'country_uz', 'language_en', 'language_ru', 'language_uz', 'image', 'file',  'created_time', 'updated_time']