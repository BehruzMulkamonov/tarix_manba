from rest_framework import serializers
from .models import Library, Comments, Library_Category, About, Feedbacks, Connection, Event, News, Sliders


class LibrariesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ['id',  'title', 'category', 'author', 'type', 'year', 'country', 'language', 'image', 'file']


class LibrariesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library_Category
        fields = ['id', 'title']


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'file']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'image']



class SlidersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sliders
        fields = ['id', 'title', 'file', 'link']



class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = ['id', 'phone', 'phone_two', 'address', 'location', 'email', 'map']



class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['id', 'title', 'content']


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedbacks
        fields = ['id', 'message']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'message']