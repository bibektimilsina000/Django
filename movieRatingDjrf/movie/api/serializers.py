from rest_framework import serializers
from ..models import Movies


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        
        return Movies.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.title=validated_data.get('title',instance.title)
       
        instance.description=validated_data.get("description",instance.description)
        instance.active=validated_data.get("active",instance.active)
        instance.save()
        return  Movies.update(instance, validated_data)