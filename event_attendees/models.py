from django.db import models
from events.models import Events
# Create your models here.

class EventAttendee(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        db_table = 'event_attendee'
        managed = True

    def __str__(self):
        return f"{self.name}-<{self.email}>"