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
    note = get_object_or_404(Note, pk=pk)
    context = {"note": note}
    return render(request, "myNotesApp/note_detail.html", context)


def note_create(request):
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
    note = get_object_or_404(Note, pk=pk)
    # Flip the pinned status
    note.pinned = not note.pinned
    note.save()
    return redirect("note_list")  # or wherever your note list is displayed


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")  # or wherever you want to redirect

    # If GET request, render a confirmation page
    return render(request, "myNotesApp/note_delete.html", {"note": note})
