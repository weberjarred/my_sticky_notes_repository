"""
This file defines the Note model with fields for title, content,
and timestamps.

Defensive programming is applied via field limits.

The Note model uses a max length for the title and applies
a maximum length validator on content (e.g. 500 characters).

Timestamps are also added for creation and modification.
"""

from django.db import models
from django.core.validators import MaxLengthValidator


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(validators=[MaxLengthValidator(500)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False)  # New field for pinning notes

    def __str__(self):
        return self.title
