from .models import Events
from rest_framework.serializers import ModelSerializer

class EventSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'