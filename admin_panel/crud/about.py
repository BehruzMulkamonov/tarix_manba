from django.http import Http404
from rest_framework import generics
from other_app.models import About
from admin_panel.serializer.about import AboutAdminSerializer
from admin_panel.pagination import ResultsSetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# class AboutListCreate(generics.ListCreateAPIView):
#     queryset = About.objects.all()
#     filterset_fields = ['id', ]
#     search_fields = ['title']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     serializer_class = AboutAdminSerializer
#     pagination_class = ResultsSetPagination


# class AboutRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutAdminSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_about(request):
    serializer = AboutAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_abouts(request):
    abouts = About.objects.all().order_by("id")
    serializer = AboutAdminSerializer(abouts, many=True)
    return Response(serializer.data)

# Detail 
@api_view(['GET'])
def about_detail(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        raise Http404

    serializer = AboutAdminSerializer(about)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_about(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response({'error': 'About not found'}, status=404)

    serializer = AboutAdminSerializer(about, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_about(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response({'error': 'About not found'}, status=404)

    about.delete()
    return Response(status=204)
