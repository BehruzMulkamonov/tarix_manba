from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import News
from admin_panel.serializer.news import NewsAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class NewsListCreate(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['title']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination

# class NewsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsAdminSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create (Yaratish)
@api_view(['POST'])
def create_news(request):
    serializer = NewsAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_news(request):
    news = News.objects.all().order_by("id")
    serializer = NewsAdminSerializer(news, many=True)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_news(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=404)

    serializer = NewsAdminSerializer(news, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_news(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=404)

    news.delete()
    return Response(status=204)
