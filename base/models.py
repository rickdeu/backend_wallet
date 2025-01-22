import uuid
from django.db import models
class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text='Date and time when the object was created.')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, help_text='Date and time when the object was last updated.')
    class Meta:
        abstract = True