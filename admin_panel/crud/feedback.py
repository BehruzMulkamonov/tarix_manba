from django.http import Http404
from other_app.models import Feedbacks
from admin_panel.serializer.feedback import FeedbacksAdminSerializer, FeedbacksAdminSerializerList
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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
    paginator = PageNumberPagination()
    paginator.page_size = 10
    feedbacks = Feedbacks.objects.all().order_by("id")
    result_page = paginator.paginate_queryset(feedbacks, request)
    serializer = FeedbacksAdminSerializerList(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# Detail
@api_view(['GET'])
def feedbacks_detail(request, pk):
    try:
        feedback = Feedbacks.objects.get(pk=pk)
    except Feedbacks.DoesNotExist:
        raise Http404

    serializer = FeedbacksAdminSerializerList(feedback)
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
