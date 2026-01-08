from django.contrib import admin

from notes.apps import NotesConfig
from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ...
