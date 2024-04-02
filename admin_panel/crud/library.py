from rest_framework import generics
from other_app.models import Library
from admin_panel.serializer.library import LibrarySerializer

class LibraryListCreate(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
