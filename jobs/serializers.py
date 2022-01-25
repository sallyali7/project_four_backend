from rest_framework import serializers
from .models import Jobs



class JobSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing job requests'''
    class Meta:
        model = Jobs
        fields = '__all__' 

