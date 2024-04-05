from rest_framework import generics
from admin_panel.pagination import ResultsSetPagination
from other_app.models import Feedbacks
from admin_panel.serializer.feedback import FeedbacksAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class FeedbacksListCreate(generics.ListCreateAPIView):
#     queryset = Feedbacks.objects.all()
#     serializer_class = FeedbacksAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['message']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination


# class FeedbacksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Feedbacks.objects.all()
#     serializer_class = FeedbacksAdminSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_feedback(request):
    serializer = FeedbacksAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_feedbacks(request):
    feedbacks = Feedbacks.objects.all().order_by("id")
    serializer = FeedbacksAdminSerializer(feedbacks, many=True)
    return Response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_feedback(request, pk):
    try:
        feedback = Feedbacks.objects.get(pk=pk)
    except Feedbacks.DoesNotExist:
        return Response({'error': 'Feedback not found'}, status=404)

    serializer = FeedbacksAdminSerializer(feedback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_feedback(request, pk):
    try:
        feedback = Feedbacks.objects.get(pk=pk)
    except Feedbacks.DoesNotExist:
        return Response({'error': 'Feedback not found'}, status=404)

    feedback.delete()
    return Response(status=204)
