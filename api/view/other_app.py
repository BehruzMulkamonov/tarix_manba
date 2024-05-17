from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from admin_panel.crud.about import AboutFilter
from admin_panel.crud.connection_value import ConnectionValFilter
from admin_panel.crud.event import EventFilter
from admin_panel.crud.feedback import FeedbackFilter
from admin_panel.crud.library import LibraryFilter
from admin_panel.crud.library_category import LibraryCatFilter
from admin_panel.crud.news import NewsFilter
from admin_panel.crud.sliders import SlidersFilter
from api.pagination import ResultsSetPagination
from other_app.models import Comments, Connection, About, Connection_Value, Event, Feedbacks, Library_Category, Library, Sliders, News
from other_app.serializers import AboutSerializer, CommentSerializer, ConnectionSerializer, ConnectionValueSerializer, EventSerializer,FeedbackSerializer, LibrariesSerializer, NewsSerializer, LibrariesCategorySerializer, SlidersSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

# Library

# Read (O'qish)
@api_view(['GET'])
def list_libraries(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    libraries = Library.objects.all().order_by("id")
    library_filter = LibraryFilter(request.GET, queryset=libraries)
    result_page = paginator.paginate_queryset(library_filter.qs, request)
    serializer = LibrariesSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def library_detail(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        raise Http404

    serializer = LibrariesSerializer(library)
    return Response(serializer.data)


# Library category

# Read (O'qish)
@api_view(['GET'])
def list_library_categories(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    categories = Library_Category.objects.all().order_by("id")
    library_cat__filter = LibraryCatFilter(request.GET, queryset=categories)
    result_page = paginator.paginate_queryset(library_cat__filter.qs, request)
    serializer = LibrariesCategorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def library_category_detail(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        raise Http404

    serializer = LibrariesCategorySerializer(category)
    return Response(serializer.data)

# About    

# Read (O'qish)
@api_view(['GET'])
def list_abouts(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    abouts = About.objects.all().order_by("id")
    about_filter = AboutFilter(request.GET, queryset=abouts)
    result_page = paginator.paginate_queryset(about_filter.qs, request)
    serializer = AboutSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail 
@api_view(['GET'])
def about_detail(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        raise Http404

    serializer = AboutSerializer(about)
    return Response(serializer.data)
    
# Event
# Read (O'qish)
@api_view(['GET'])
def list_events(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    events = Event.objects.all().order_by("id")
    event_filter = EventFilter(request.GET, queryset=events)
    result_page = paginator.paginate_queryset(event_filter.qs, request)
    serializer = EventSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404

    serializer = EventSerializer(event)
    return Response(serializer.data)

# News
# Read (O'qish)
@api_view(['GET'])
def list_news(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    news = News.objects.all().order_by("id")
    news_filter = NewsFilter(request.GET, queryset=news)
    result_page = paginator.paginate_queryset(news_filter.qs, request)
    serializer = NewsSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def news_detail(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsSerializer(news)
    return Response(serializer.data)


# Read (O'qish)
@api_view(['GET'])
def list_sliders(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    sliders = Sliders.objects.all().order_by("id")
    sliders_filter = SlidersFilter(request.GET, queryset=sliders)
    result_page = paginator.paginate_queryset(sliders_filter.qs, request)
    serializer = SlidersSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def sliders_detail(request, pk):
    try:
        slider = Sliders.objects.get(pk=pk)
    except Sliders.DoesNotExist:
        raise Http404

    serializer = SlidersSerializer(slider)
    return Response(serializer.data)

# Connection 

# Read (O'qish)
@api_view(['GET'])
def list_connection_value(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    connections = Connection_Value.objects.all().order_by("id")
    connections_val_filter = ConnectionValFilter(request.GET, queryset=connections)
    result_page = paginator.paginate_queryset(connections_val_filter.qs, request)
    serializer = ConnectionValueSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def connection_value_detail(request, pk):
    try:
        connection = Connection_Value.objects.get(pk=pk)
    except Connection_Value.DoesNotExist:
        raise Http404

    serializer = ConnectionValueSerializer(connection)
    return Response(serializer.data)
    
# feedbacks
# Read (O'qish)
@api_view(['GET'])
def list_feedbacks(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    feedbacks = Feedbacks.objects.all().order_by("id")
    feedback_filter = FeedbackFilter(request.GET, queryset=feedbacks)
    result_page = paginator.paginate_queryset(feedback_filter.qs, request)
    serializer = FeedbackSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def feedbacks_detail(request, pk):
    try:
        feedback = Feedbacks.objects.get(pk=pk)
    except Feedbacks.DoesNotExist:
        raise Http404

    serializer = FeedbackSerializer(feedback)
    return Response(serializer.data)