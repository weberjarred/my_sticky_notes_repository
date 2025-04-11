"""
This creates a ModelForm for Note that includes input validation
and defensive programming (e.g. by cleaning inputs made).

The clean methods ensure that empty inputs are caught and unnecessary
whitespace removed.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    NoteForm is a Django ModelForm for the Note model. It provides form fields
    for the "title" and "content" attributes of the Note model and includes
    custom validation logic for these fields.

    Methods:
        clean_title():
            Validates the "title" field to ensure it is not empty. Strips any
            leading or trailing whitespace from the input. Raises a
            ValidationError if the field is empty.
        clean_content():
            Validates the "content" field to ensure it is not empty. Strips any
            leading or trailing whitespace from the input. Raises a
            ValidationError if the field is empty.
    """
    class Meta:
        """
        Meta class for the form, specifying the model and the fields to
        include.
        - `model`: Specifies the model (`Note`) that this form is associated
          with.
        - `fields`: A list of fields (`["title", "content"]`) from the model
          to be included in the form.
        """
        model = Note
        fields = ["title", "content"]

    def clean_title(self):
        """
        Validates and cleans the 'title' field in a form.

        This method checks if the 'title' field is not empty. If the field is
        empty, it raises a ValidationError. Otherwise, it returns the stripped
        version of the title.

        Returns:
            str: The cleaned and stripped title.

        Raises:
            forms.ValidationError: If the 'title' field is empty.
        """
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title.strip()

    def clean_content(self):
        """
        Validates and cleans the 'content' field in the form.

        This method checks if the 'content' field is empty and raises a
        ValidationError if it is. If the field contains data, it strips
        any leading or trailing whitespace and returns the cleaned value.

        Returns:
            str: The cleaned and stripped content value.

        Raises:
            forms.ValidationError: If the 'content' field is empty.
        """
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        return content.strip()
