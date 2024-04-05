from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import Comments
from admin_panel.serializer.comment import CommentsAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# class CommentsListCreate(generics.ListCreateAPIView):
#     queryset = Comments.objects.all()
#     filterset_fields = ['id', ]
#     search_fields = ['message']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination
#     serializer_class = CommentsAdminSerializer

# class CommentsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsAdminSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_comment(request):
    serializer = CommentsAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_comments(request):
    comments = Comments.objects.all().order_by("id")
    serializer = CommentsAdminSerializer(comments, many=True)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=404)

    serializer = CommentsAdminSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=404)

    comment.delete()
    return Response(status=204)
