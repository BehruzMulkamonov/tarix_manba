from django.http import Http404
from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import Event
from admin_panel.serializer.event import EventAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class EventListCreate(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['title']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination


# class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventAdminSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    events = Event.objects.all().order_by("id")
    serializer = EventAdminSerializer(events, many=True)
    return Response(serializer.data)

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
