from django.urls import path
from .views import EventsListAPIView, RegisterAttendeeCreateView, EventAttendeesListAPIView

urlpatterns = [
    path('', EventsListAPIView.as_view(), name='events-list-create'),
    path('<int:id>/register/', RegisterAttendeeCreateView.as_view(), name='attendee-create'),
    path('<int:id>/attendees/', EventAttendeesListAPIView.as_view(),
         name='event-attendee-list'),
]
