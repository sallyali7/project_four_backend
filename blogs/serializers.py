from rest_framework import serializers
from .models import Blogs

class BlogSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing blog requests'''
    class Meta:
        model = Blogs
        fields = '__all__' 
