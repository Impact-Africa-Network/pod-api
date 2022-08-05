from rest_framework import serializers
from .models import Podcasts

class PodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Podcasts
        # fields=['id','full_name','ld_number','date_listened','podcast_name','podcast_link','podcast_category','podcast_group','podcast_notes','owner','points']
        fields=['id','full_name','ld_number','date_listened','podcast_name','podcast_link','podcast_category','podcast_group','podcast_notes','points']