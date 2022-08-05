from rest_framework import serializers
from .models import Connections

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Connections
        # fields=['id','full_name','ld_number','person_met','date_met','meeting_details','fun_fact','owner','points']
        fields=['id','full_name','ld_number','person_met','date_met','meeting_details','fun_fact','points']