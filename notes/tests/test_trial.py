from django.test import TestCase
from django.contrib.auth import get_user_model

from notes.models import Note


User = get_user_model()


class TestNotes(TestCase):
    TITLE = 'заголовок заметки'
    TEXT = 'Текст заметки'
    SLUG = 'originalslug'

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Maxim')
        cls.note = Note.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
            slug=cls.SLUG,
            author=cls.author,
        )

    def test_successful_creation(self):
        notes_count = Note.objects.count()
        print(f'создалась {notes_count} заметка')
        self.assertEqual(notes_count, 1, 'ОШИБКА')

    def test_title(self):
        self.assertEqual(self.note.title, self.TITLE, 'TITLE не совпадает')
