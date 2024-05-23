from rest_framework import serializers
from .models import Connection_Value, Library, Comments, Library_Category, About, Feedbacks, Connection, Event, News, Sliders


class LibrariesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ['id',  'title', 'category', 'author', 'type', 'year', 'country', 'language', 'image', 'file', 'created_time', 'updated_time']


class LibrariesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library_Category
        fields = ['id', 'title', 'created_time', 'updated_time']


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'file', 'created_time', 'updated_time']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'image', 'created_time', 'updated_time']



class SlidersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sliders
        fields = ['id', 'title', 'file', 'link', 'created_time', 'updated_time']



class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = ['id', 'phone', 'phone_two', 'address', 'location', 'email', 'map', 'created_time', 'updated_time']



class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['id', 'title', 'content', 'created_time', 'updated_time']


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedbacks
        fields = ['id', 'message', 'created_time', 'updated_time']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'message', 'created_time', 'updated_time']


class ConnectionValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection_Value
        fields = ['id', 'connection_category', 'value', 'created_time', 'updated_time']