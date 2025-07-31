from .models import Events
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils.timezone import make_aware, localtime
import pytz

class EventSerializer(ModelSerializer):
    timezone = serializers.CharField(write_only=True)

    class Meta:
        model = Events
        fields = '__all__'

    def validate(self, attrs):
        tz_str = attrs.get('timezone')
        try:
            user_tz = pytz.timezone(tz_str)
        except pytz.UnknownTimeZoneError:
            raise serializers.ValidationError({'timezone': 'Invalid timezone.'})

        start = attrs.get('start_time')
        end = attrs.get('end_time')

        if start and not start.tzinfo:
            start = make_aware(start, timezone=user_tz)
        if end and not end.tzinfo:
            end = make_aware(end, timezone=user_tz)

        if start >= end:
            raise serializers.ValidationError("Start time must be before end time.")

        attrs['start_time'] = start.astimezone(pytz.UTC)
        attrs['end_time'] = end.astimezone(pytz.UTC)
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            tz = pytz.timezone(instance.timezone)
            data['start_time'] = localtime(instance.start_time, timezone=tz).isoformat()
            data['end_time'] = localtime(instance.end_time, timezone=tz).isoformat()
        except Exception:
            pass
        return data
