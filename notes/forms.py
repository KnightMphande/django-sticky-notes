"""Forms used to create and update sticky notes."""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Collect and validate the editable fields of a note."""

    class Meta:
        """Configure the model and fields represented by the form."""

        model = Note
        fields = ["title", "content"]
