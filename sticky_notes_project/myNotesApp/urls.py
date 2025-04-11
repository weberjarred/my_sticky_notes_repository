"""
This file maps URL patterns to the views.

→ URL patterns follow RESTful conventions.
"""

from django.urls import path
from . import views
from .views import note_list, note_delete, note_toggle_pin

urlpatterns = [
    path("", note_list, name="note_list"),
    path("note/<int:pk>/", views.note_detail, name="note_detail"),
    path("note/new/", views.note_create, name="note_create"),
    path("note/<int:pk>/edit/", views.note_update, name="note_update"),
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
    path("note/<int:pk>/toggle_pin/", note_toggle_pin, name="note_toggle_pin"),
]
