from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import Library_Category
from admin_panel.serializer.library_category import Library_CategoryAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class Library_CategoryListCreate(generics.ListCreateAPIView):
#     queryset = Library_Category.objects.all()
#     serializer_class = Library_CategoryAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['title']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination

# class Library_CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Library_Category.objects.all()
#     serializer_class = Library_CategoryAdminSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_library_category(request):
    serializer = Library_CategoryAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_library_categories(request):
    categories = Library_Category.objects.all().order_by("id")
    serializer = Library_CategoryAdminSerializer(categories, many=True)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_library_category(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        return Response({'error': 'Library Category not found'}, status=404)

    serializer = Library_CategoryAdminSerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_library_category(request, pk):
    try:
        category = Library_Category.objects.get(pk=pk)
    except Library_Category.DoesNotExist:
        return Response({'error': 'Library Category not found'}, status=404)

    category.delete()
    return Response(status=204)
