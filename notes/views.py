"""Class-based views for creating, reading, updating and deleting notes."""

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    """Display all notes on the application's home page."""

    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"


class NoteDetailView(DetailView):
    """Display the complete content of one selected note."""

    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"


class NoteCreateView(CreateView):
    """Display and process the form used to create a note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")


class NoteUpdateView(UpdateView):
    """Display and process the form used to edit an existing note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")


class NoteDeleteView(DeleteView):
    """Ask for confirmation and delete the selected note."""

    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note_list")
