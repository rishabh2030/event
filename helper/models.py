from django.db import models

class TimestampMixin(models.Model):
    """A mixin for adding creation and modification timestamps to models."""

    id = models.AutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp indicating when the instance was created.")
    modified_at = models.DateTimeField(auto_now=True, help_text="Timestamp indicating when the instance was last modified.")

    class Meta:
        abstract = True
