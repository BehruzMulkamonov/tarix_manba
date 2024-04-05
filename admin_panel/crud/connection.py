from admin_panel.pagination import ResultsSetPagination
from other_app.models import Connection
from admin_panel.serializer.connection import ConnectionAdminSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# class ConnectionListCreate(generics.ListCreateAPIView):
#     queryset = Connection.objects.all()
#     serializer_class = ConnectionAdminSerializer
#     filterset_fields = ['id', ]
#     search_fields = ['email']
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     pagination_class = ResultsSetPagination


# class ConnectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Connection.objects.all()
#     serializer_class = ConnectionAdminSerializer


###############
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create (Yaratish)
@api_view(['POST'])
def create_connection(request):
    serializer = ConnectionAdminSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Read (O'qish)
@api_view(['GET'])
def list_connections(request):
    connections = Connection.objects.all().order_by("id")
    serializer = ConnectionAdminSerializer(connections, many=True)
    # paginator = ResultsSetPagination()
    return Response(serializer.data)
    # return paginator.get_paginated_response(serializer.data)

# Update (Yangilash)
@api_view(['PUT'])
def update_connection(request, pk):
    try:
        connection = Connection.objects.get(pk=pk)
    except Connection.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    serializer = ConnectionAdminSerializer(connection, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete (O'chirish)
@api_view(['DELETE'])
def delete_connection(request, pk):
    try:
        connection = Connection.objects.get(pk=pk)
    except Connection.DoesNotExist:
        return Response({'error': 'Connection not found'}, status=404)

    connection.delete()
    return Response(status=204)

