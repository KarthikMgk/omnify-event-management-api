from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from .models import Events
from event_attendees.models import EventAttendee
from event_attendees.serializers import EventAttendeeSerializer, ListEventAttendeeSerializer
from .serializers import EventSerializer
from rest_framework.exceptions import ValidationError

# Create your views here.
class EventsListAPIView(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class RegisterAttendeeCreateView(CreateAPIView):
    queryset = EventAttendee.objects.all()
    serializer_class = EventAttendeeSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs['id']
        print(self.request.data, " is the payload")
        try:
            event = Events.objects.get(id=event_id)
        except Events.DoesNotExist:
            raise ValidationError('Event not found')
        
        current_attendee_count = event.attendees.count()
        if current_attendee_count > event.max_capacity:
            raise ValidationError('Registration closed: max capacity reached')
        
        serializer.save(event=event)

class EventAttendeesListAPIView(ListAPIView):
    queryset = EventAttendee.objects.all()
    serializer_class = ListEventAttendeeSerializer
