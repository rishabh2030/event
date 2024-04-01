from django.db import models
from helper.models import TimestampMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(TimestampMixin):
    """
    Represents an event in the system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    organizer_name = models.CharField(max_length=100, null=True, blank=True)
    rsvp_option = models.BooleanField(default=True)

    def __str__(self):
        """
        String representation of the event object.
        """
        return self.title if self.title else "Untitled Event"
