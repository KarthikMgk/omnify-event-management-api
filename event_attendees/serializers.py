from .models import EventAttendee
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class EventAttendeeSerializer(ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'
        read_only_fields = ['event']
    
    def validate_email(self, value):
        if EventAttendee.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value
    

class ListEventAttendeeSerializer(ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'