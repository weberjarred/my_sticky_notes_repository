"""
This file contains CRUD views for handling Note creation,
display, update, and deletion.

Defensive programming techniques are also used to handle
invalid user requests.

→ Each view uses Django shortcuts for error handling and redirection.
→ The POST methods are checked, and in case of invalid form data
  the form is re-rendered with error messages.
→ For deletion, a confirmation page is rendered if the request is
  not POST.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Handles the display and creation of notes.
    This view function processes both GET and POST requests. For GET requests,
    it renders a list of notes ordered by their pinned status (descending) and
    creation date (newest first). For POST requests, it processes the submitted
    form data to create a new note, and then redirects back to the note list.

    Args:
        request (HttpRequest): The HTTP request object containing metadata
        about the request.

    Returns:
        HttpResponse: Renders the 'note_list.html' template with the form and
        the list of notes, or redirects to the note list after a successful
        form submission.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    # Order by pinned (desc) first, then by newest creation
    notes = Note.objects.all().order_by("-pinned", "-created_at")
    return render(
        request, "myNotesApp/note_list.html", {"form": form, "notes": notes}
    )


def note_detail(request, pk):
    """
    View function to display the details of a specific note.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note to retrieve.

    Returns:
        HttpResponse: The rendered HTML page displaying the note details.

    Raises:
        Http404: If the note with the given primary key does not exist.
    """
    note = get_object_or_404(Note, pk=pk)
    context = {"note": note}
    return render(request, "myNotesApp/note_detail.html", context)


def note_create(request):
    """
    Handle the creation of a new note.

    This view processes both GET and POST requests. For GET requests, it
    renders a blank note creation form. For POST requests, it validates
    the submitted form data and, if valid, saves the new note and redirects
    to the note detail page. If the form is invalid, it re-renders the form
    with error messages.

    Args:
        request (HttpRequest): The HTTP request object containing metadata
        about the request.

    Returns:
        HttpResponse: A response object that either renders the note creation
        form or redirects to the detail page of the newly created note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect("note_detail", pk=note.pk)
        else:
            return render(request, "myNotesApp/note_form.html", {"form": form})
    else:
        form = NoteForm()
    return render(request, "myNotesApp/note_form.html", {"form": form})


def note_update(request, pk):
    """
    Handle the update of an existing note.

    This view retrieves a note by its primary key (pk) and allows the user
    to update it.
    If the request method is POST, it processes the submitted form data
    and updates the note if the form is valid. Otherwise, it re-renders
    the form with validation errors. If the request method is not POST,
    it displays the form pre-filled with the note's current data.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note to be updated.

    Returns:
        HttpResponse: A redirect to the note detail page if the form is
        successfully submitted.
        Otherwise, renders the note form template with the form context.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect("note_detail", pk=note.pk)
        else:
            return render(request, "myNotesApp/note_form.html", {"form": form})
    else:
        form = NoteForm(instance=note)
    return render(request, "myNotesApp/note_form.html", {"form": form})


def note_toggle_pin(request, pk):
    """
    Toggle the pinned status of a specific note.

    This view retrieves a note by its primary key (pk) and flips its
    pinned status (True to False or False to True). After updating
    the note, it redirects the user to the note list or another
    specified view.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note to be toggled.

    Returns:
        HttpResponseRedirect: A redirect to the note list or another
        specified view after toggling the pinned status.
    """
    note = get_object_or_404(Note, pk=pk)
    # Flip the pinned status
    note.pinned = not note.pinned
    note.save()
    return redirect("note_list")  # or wherever your note list is displayed


def note_delete(request, pk):
    """
    Handles the deletion of a specific note.
    This view retrieves a note by its primary key (pk) and deletes it if the
    request method is POST. If the request method is GET, it renders a
    confirmation page to ensure the user wants to delete the note.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the note to be deleted.

    Returns:
        HttpResponse: A redirect to the "note_list" view after successful
        deletion if the request method is POST.
        HttpResponse: A rendered confirmation page if the request method is
        GET. This ensures the user confirms the deletion.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")  # or wherever you want to redirect

    # If GET request, render a confirmation page
    return render(request, "myNotesApp/note_delete.html", {"note": note})
