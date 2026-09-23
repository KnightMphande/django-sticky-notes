"""Database models for the notes application."""

from django.db import models


class Note(models.Model):
    """Represent a single sticky note stored by the application."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note title for readable admin and shell output."""

        return self.title
