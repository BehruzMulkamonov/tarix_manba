from django.http import Http404
from other_app.models import Event
from admin_panel.serializer.event import EventAdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import django_filters


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')  # content nomli maydon uchun filtirlash
    class Meta:
        model = Event
        fields = ['title', 'content']


# Create (Yaratish)
@api_view(['POST'])
def create_event(request):
    serializer = EventAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_events(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    events = Event.objects.all().order_by("id")
    event_filter = EventFilter(request.GET, queryset=events)
    result_page = paginator.paginate_queryset(event_filter.qs, request)
    serializer = EventAdminSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404

    serializer = EventAdminSerializer(event)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)

    serializer = EventAdminSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)

    event.delete()
    return Response(status=204)
