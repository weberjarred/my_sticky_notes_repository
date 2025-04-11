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
    """
    Test case for the Note model.

    This test case includes unit tests for the Note model to ensure its
    functionality and behaviour are as expected.

    Methods:
        setUp():
            Sets up a sample Note instance for testing purposes.
        test_note_str():
            Tests the __str__ method of the Note model to ensure it
            returns the title.
    """
    def setUp(self):
        """
        setUp method to prepare the test environment before each test case.

        This method creates a sample Note object with a title and content
        to be used in the test cases. It ensures that each test starts
        with a consistent and predictable state.
        """
        # Arrange: Create a sample note for testing
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_str(self):
        """
        Test case for the __str__ method of the Note model.

        This test ensures that the string representation of a Note instance
        correctly returns the title of the note.
        """
        # Assert: Check that __str__ returns the title
        self.assertEqual(str(self.note), "Test Note")


class NoteViewTest(TestCase):
    """
    Test suite for the views in the myNotesApp application.
    This test case verifies the behaviour of the note list and detail views.

    Classes:
        NoteViewTest: Contains tests for the note list and detail views.

    Methods:
        setUp():
            Sets up the test environment by creating a sample note for testing.
        test_note_list_view():
            Tests the note list view to ensure it returns a 200 status code
            and displays the created note's title.
        test_note_detail_view():
            Tests the note detail view to ensure it returns a 200 status code
            and displays the created note's title and content.
    """
    def setUp(self):
        """
        Set up the test environment by creating a Note instance.

        This method is called before each test case to prepare the necessary
        data for testing. It creates a Note object with a predefined title
        and content, which can be used in view-related test cases.
        """
        # Arrange: Create a note to use in view tests
        self.note = Note.objects.create(
            title="View Test Note", content="Content for view testing."
        )

    def test_note_list_view(self):
        """
        Tests the note list view.

        This test ensures that the note list view is accessible and returns the
        correct HTTP status code (200). It also verifies that the response
        contains the expected content, specifically the text "View Test Note".
        """
        # Act: Access the note list view
        response = self.client.get(reverse("note_list"))
        # Assert: Verify response code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")

    def test_note_detail_view(self):
        """
        Test the note detail view.

        This test verifies that the note detail view is accessible and displays
        the correct details for a specific note.

        Test Steps:
        1. Perform a GET request to the note detail view using the note's
           primary key.
        2. Assert that the response status code is 200 (OK).
        3. Assert that the response contains the expected note title.
        4. Assert that the response contains the expected note content.
        """
        # Act: Access the note detail view
        response = self.client.get(
            reverse("note_detail", kwargs={"pk": self.note.pk})
        )
        # Assert: Verify response code and that details are shown
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")
        self.assertContains(response, "Content for view testing.")


class NoteFormTest(TestCase):
    """
    Test suite for validating the NoteForm in the myNotesApp.

    Classes:
        NoteFormTest: Contains unit tests for validating the behaviour of the
        NoteForm.

    Methods:
        test_valid_note_form:
            Tests that the form is valid when provided with valid data.
            - Ensures that the form accepts a title and content
              that meet the requirements.
        test_invalid_note_form:
            Tests that the form is invalid when provided with invalid data.
            - Ensures that an empty title results in form validation errors.
            - Verifies that the "title" field is included in the form's error
              messages.
    """
    def test_valid_note_form(self):
        """
        Test case for validating the NoteForm with valid input data.

        This test ensures that the NoteForm correctly identifies valid input
        data and returns a valid form instance.

        Steps:
        1. Arrange: Prepare a dictionary with valid title and content
           for the form.
        2. Act: Create a NoteForm instance using the valid data.
        3. Assert: Verify that the form instance is valid using `is_valid()`.

        Expected Outcome:
        - The form should be valid when provided with the specified valid data.
        """
        # Arrange: Prepare valid data
        data = {"title": "Form Test Note", "content": "Valid content."}
        form = NoteForm(data=data)
        # Act & Assert: Form should be valid
        self.assertTrue(form.is_valid())

    def test_invalid_note_form(self):
        """
        Test case for validating the NoteForm with invalid input.

        This test ensures that the form is invalid when the title field is
        empty.

        It verifies that:
        - The form's `is_valid()` method returns False.
        - The "title" field is included in the form's error messages.
        """
        # Arrange: Provide empty title which should fail
        data = {"title": "", "content": "Content without a title."}
        form = NoteForm(data=data)
        # Act & Assert: Form should be invalid
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
