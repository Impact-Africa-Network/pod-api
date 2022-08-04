from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Podcasts
from .serializers import PodcastsSerializer

# Create your views here.
@api_view(['GET','POST'])
def podcasts_list(request, format=None):
    # gets all podcasts for  the logged user 
    if request.method=='GET':
        podcasts=Podcasts.objects.all()
        serializer=PodcastsSerializer(podcasts, many=True)
        return Response(serializer.data)
    # creates a new podcast for logged user 
    if request.method=='POST':
        serializer=PodcastsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE',])
def podcast_detail(request,pk, format=None):
    try:
        podcast=Podcasts.objects.get(pk=pk)
    except Podcasts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # fetch a single podcast 
    if request.method=='GET':
        serializer=PodcastsSerializer(podcast)
        return Response(serializer.data)
    # updates single podcast 
    if request.method=='PUT':
        serializer=PodcastsSerializer(podcast,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # detes single podcast 
    if request.method=='DELTE':
        podcast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
