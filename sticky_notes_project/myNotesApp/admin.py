"""
Register the Note model so that it can be managed
via the Django admin interface.
"""

from django.contrib import admin
from .models import Note

# Register the Note model with the admin site, through admin interface.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    NoteAdmin is a custom admin class for managing Note objects in the Django
    admin interface.

    Attributes:
        list_display (tuple): Specifies the fields to display in the admin list
        view.
            In this case, "title" and "created_at" are displayed.
        search_fields (tuple): Specifies the fields to include in the search
            functionality within the admin interface. Here, "title" and
            "content" are searchable.
    """
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
