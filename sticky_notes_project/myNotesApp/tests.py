"""
Unit tests for models and views.

→ Tests follow the AAA (Arrange–Act–Assert) pattern and the FIRST
  principles (Fast, Independent, Repeatable, Self-validating, Timely).

→ Each test method is organized into arrange, act, and assert sections.
→ The tests cover the model’s string representation, the list/detail
  views, and form validation.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteModelTest(TestCase):
    def setUp(self):
        # Arrange: Create a sample note for testing
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_str(self):
        # Assert: Check that __str__ returns the title
        self.assertEqual(str(self.note), "Test Note")


class NoteViewTest(TestCase):
    def setUp(self):
        # Arrange: Create a note to use in view tests
        self.note = Note.objects.create(
            title="View Test Note", content="Content for view testing."
        )

    def test_note_list_view(self):
        # Act: Access the note list view
        response = self.client.get(reverse("note_list"))
        # Assert: Verify response code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")

    def test_note_detail_view(self):
        # Act: Access the note detail view
        response = self.client.get(
            reverse("note_detail", kwargs={"pk": self.note.pk})
        )
        # Assert: Verify response code and that details are shown
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")
        self.assertContains(response, "Content for view testing.")


class NoteFormTest(TestCase):
    def test_valid_note_form(self):
        # Arrange: Prepare valid data
        data = {"title": "Form Test Note", "content": "Valid content."}
        form = NoteForm(data=data)
        # Act & Assert: Form should be valid
        self.assertTrue(form.is_valid())

    def test_invalid_note_form(self):
        # Arrange: Provide empty title which should fail
        data = {"title": "", "content": "Content without a title."}
        form = NoteForm(data=data)
        # Act & Assert: Form should be invalid
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
