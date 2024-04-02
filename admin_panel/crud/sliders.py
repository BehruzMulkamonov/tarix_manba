from rest_framework import generics
from other_app.models import Sliders
from admin_panel.serializer.sliders import SlidersSerializer

class SlidersListCreate(generics.ListCreateAPIView):
    queryset = Sliders.objects.all()
    serializer_class = SlidersSerializer

class SlidersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sliders.objects.all()
    serializer_class = SlidersSerializer
