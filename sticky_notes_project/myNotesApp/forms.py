"""
This creates a ModelForm for Note that includes input validation
and defensive programming (e.g. by cleaning inputs made).

The clean methods ensure that empty inputs are caught and unnecessary
whitespace removed.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title.strip()

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        return content.strip()
