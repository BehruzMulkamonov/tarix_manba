from rest_framework import generics
from other_app.models import Connection
from admin_panel.serializer.connection import ConnectionSerializer

class ConnectionListCreate(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class ConnectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
