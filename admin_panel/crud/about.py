from datetime import datetime
from django.http import Http404
from other_app.models import About
from admin_panel.serializer.about import AboutAdminSerializer, AboutAdminSerializerList
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_about(request):
    serializer = AboutAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_time=datetime.now())
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Read (O'qish)
@api_view(['GET'])
def list_abouts(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    abouts = About.objects.all().order_by("id")
    result_page = paginator.paginate_queryset(abouts, request)
    serializer = AboutAdminSerializerList(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail 
@api_view(['GET'])
def about_detail(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        raise Http404

    serializer = AboutAdminSerializerList(about)
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
        serializer.save(updated_time=datetime.now())
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
