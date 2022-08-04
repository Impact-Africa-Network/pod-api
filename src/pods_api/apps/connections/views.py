from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Connections
from .serializers import ConnectionsSerializer

# Create your views here.
@api_view(['GET','POST'])
def connections_list(request, format=None):
    # gets all connections for  the logged user 
    if request.method=='GET':
        connections=Connections.objects.all()
        serializer=ConnectionsSerializer(connections, many=True)
        return Response(serializer.data)
    # creates a new connection for logged user 
    if request.method=='POST':
        serializer=ConnectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE',])
def connection_detail(request,pk, format=None):
    try:
        connect=Connections.objects.get(pk=pk)
    except Connections.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # fetch a single connection 
    if request.method=='GET':
        serializer=ConnectionsSerializer(connect)
        return Response(serializer.data)
    # updates single connection 
    if request.method=='PUT':
        serializer=ConnectionsSerializer(connect,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # detes single connection 
    if request.method=='DELTE':
        connect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
