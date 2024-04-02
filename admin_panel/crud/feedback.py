from rest_framework import generics
from other_app.models import Feedbacks
from admin_panel.serializer.feedback import FeedbacksSerializer

class FeedbacksListCreate(generics.ListCreateAPIView):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer

class FeedbacksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
