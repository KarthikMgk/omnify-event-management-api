from .models import EventAttendee
from events.models import Events
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class EventAttendeeSerializer(ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'
        read_only_fields = ['event']
    

    def validate_email(self, value):
        print('calling validate_email')
        event_id = self.context.get('event_id')
        if not event_id:
            raise serializers.ValidationError('Event ID not provided in context.')

        try:
            event_object = Events.objects.get(id=int(event_id))
            print(event_object)
        except Events.DoesNotExist:
            raise serializers.ValidationError('Event does not exist.')
        
        print(EventAttendee.objects.filter(
            email=value, event=event_object).exists())

        if EventAttendee.objects.filter(email=value, event=event_object).exists():
            raise serializers.ValidationError(
                'This email is already registered for the event.')

        return value
    

class ListEventAttendeeSerializer(ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'