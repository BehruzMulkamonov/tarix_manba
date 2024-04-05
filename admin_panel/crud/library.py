from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import Library
from admin_panel.serializer.library import LibraryAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class LibraryListCreate(generics.ListCreateAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibraryAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['title']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination

# class LibraryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibraryAdminSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create (Yaratish)
@api_view(['POST'])
def create_library(request):
    serializer = LibraryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_libraries(request):
    libraries = Library.objects.all().order_by("id")
    serializer = LibraryAdminSerializer(libraries, many=True)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response({'error': 'Library not found'}, status=404)

    serializer = LibraryAdminSerializer(library, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response({'error': 'Library not found'}, status=404)

    library.delete()
    return Response(status=204)
