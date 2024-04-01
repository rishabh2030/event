from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.
    """
    class Meta:
        model = Event
        fields = ('id', 'user', 'title', 'description', 'date', 'time', 'location', 'organizer_name', 'rsvp_option')
