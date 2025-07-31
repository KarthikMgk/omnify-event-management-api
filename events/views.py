from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from .models import Events
from event_attendees.models import EventAttendee
from event_attendees.serializers import EventAttendeeSerializer, ListEventAttendeeSerializer
from .serializers import EventSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async, async_to_sync
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(
    summary="List and create events",
    description="Retrieve a list of all events or create a new event.",
    responses={200: EventSerializer(many=True)},
    request=EventSerializer
)
class EventsListAPIView(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


@extend_schema(
    summary="Register for event",
    description="Register a new attendee for a specific event by ID.",
    request=EventAttendeeSerializer,
    responses={201: EventAttendeeSerializer},
)
class RegisterAttendeeCreateView(CreateAPIView):
    queryset = EventAttendee.objects.all()
    serializer_class = EventAttendeeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['event_id'] = self.kwargs['id']
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        async_to_sync(self.perform_create)(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    async def perform_create(self, serializer):
        event_id = self.kwargs['id']
        try:
            event = await sync_to_async(Events.objects.get)(id=event_id)
        except Events.DoesNotExist:
            raise ValidationError('Event not found')
        
        current_attendee_count = await sync_to_async(lambda: event.attendees.count())()
        if current_attendee_count > event.max_capacity:
            raise ValidationError('Registration closed: max capacity reached')
        
        await sync_to_async(serializer.save)(event=event)

@extend_schema(
    summary="List all event attendees",
    description="Get a list of all registered attendees for all events.",
    responses={200: ListEventAttendeeSerializer(many=True)}
)
class EventAttendeesListAPIView(ListAPIView):
    queryset = EventAttendee.objects.all()
    serializer_class = ListEventAttendeeSerializer
