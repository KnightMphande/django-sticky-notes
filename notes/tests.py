from django.test import TestCase
from django.urls import reverse

from .forms import NoteForm
from .models import Note


class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="My First Test",
            content="Testing Django models."
        )

        self.assertEqual(note.title, "My First Test")
        self.assertEqual(note.content, "Testing Django models.")
        self.assertIsNotNone(note.created_at)


class NoteViewTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        response = self.client.get(
            reverse("note_detail", args=[self.note.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test note.")

    def test_note_create_view(self):
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "Created Note",
                "content": "Created during testing."
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Note.objects.filter(title="Created Note").exists()
        )

    def test_note_update_view(self):
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            {
                "title": "Updated Note",
                "content": "Updated content."
            }
        )

        self.assertEqual(response.status_code, 302)

        self.note.refresh_from_db()

        self.assertEqual(self.note.title, "Updated Note")

    def test_note_delete_view(self):
        response = self.client.post(
            reverse("note_delete", args=[self.note.pk])
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Note.objects.filter(pk=self.note.pk).exists()
        )


class NoteFormTest(TestCase):

    def test_valid_form(self):
        form = NoteForm(
            data={
                "title": "Shopping",
                "content": "Buy milk"
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = NoteForm(
            data={
                "title": "",
                "content": "Buy milk"
            }
        )

        self.assertFalse(form.is_valid())
