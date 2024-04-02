from rest_framework import generics
from other_app.models import About
from admin_panel.serializer.about import AboutSerializer

class AboutListCreate(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
