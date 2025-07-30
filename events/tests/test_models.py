from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from events.models import Events
from datetime import timedelta


class EventsModelTest(TestCase):

    def setUp(self):
        print("SETUP CALLED")
        self.valid_data = {
            'name': 'Event 1',
            'location': 'Chennai',
            'start_time': timezone.now(),
            'end_time': timezone.now() + timedelta(hours=2),
            'max_capacity': 26,
        }

    def test_event_creation_success(self):
        event = Events(**self.valid_data)
        try:
            event.full_clean()
        except ValidationError:
            self.fail("Valid event raised ValidationError unexpectedly")

    def test_event_max_capacity_validation(self):
        self.valid_data['max_capacity'] = 10
        event = Events(**self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            event.full_clean()
        self.assertIn('max_capacity', cm.exception.message_dict)

    def test_start_time_after_end_time_should_raise(self):
        self.valid_data['start_time'] = timezone.now() + timedelta(hours=2)
        self.valid_data['end_time'] = timezone.now()
        event = Events(**self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            event.full_clean()
        self.assertIn('Start time must be earlier than end timeq',
                      str(cm.exception))

    def test_str_method(self):
        event = Events(**self.valid_data)
        self.assertEqual(str(event), self.valid_data['name'])
