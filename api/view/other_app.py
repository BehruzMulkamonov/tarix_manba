from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from api.pagination import ResultsSetPagination
from other_app.models import Comments, Connection, About, Event, Feedbacks, Library_Category, Library, Sliders, News
from other_app.serializers import AboutSerializer, CommentSerializer, ConnectionSerializer, EventSerializer,FeedbackSerializer, LibrariesSerializer, NewsSerializer, LibrariesCategorySerializer, SlidersSerializer
from rest_framework import filters


class LibrariesListViews(generics.ListAPIView):
    search_fields = ['author', 'title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LibrariesSerializer
    paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Library.objects.all()


class LibraryCategoryListViews(generics.ListAPIView):
    serializer_class = LibrariesCategorySerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Library_Category.objects.all()
    

class AboutListViews(generics.ListAPIView):
    serializer_class = AboutSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return About.objects.all()
    

class EventListViews(generics.ListAPIView):
    serializer_class = EventSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Event.objects.all()


class NewsListViews(generics.ListAPIView):
    serializer_class = NewsSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return News.objects.all()


class SlidersListViews(generics.ListAPIView):
    serializer_class = SlidersSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Sliders.objects.all()


class ConnectionListViews(generics.ListAPIView):
    serializer_class = ConnectionSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Connection.objects.all()
    

class CommentListViews(generics.ListAPIView):
    serializer_class = CommentSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Comments.objects.all()
    

class FeedbackListViews(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    # paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Feedbacks.objects.all()