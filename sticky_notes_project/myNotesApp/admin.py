"""
Register the Note model so that it can be managed
via the Django admin interface.
"""

from django.contrib import admin
from .models import Note

# Register the Note model with the admin site, through admin interface.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
