from rest_framework import generics
from other_app.models import Library_Category
from admin_panel.serializer.library_category import Library_CategorySerializer

class Library_CategoryListCreate(generics.ListCreateAPIView):
    queryset = Library_Category.objects.all()
    serializer_class = Library_CategorySerializer

class Library_CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library_Category.objects.all()
    serializer_class = Library_CategorySerializer
