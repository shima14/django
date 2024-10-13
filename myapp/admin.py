from django.contrib import admin
from .models import MarkdownPage

@admin.register(MarkdownPage)
class MarkdownPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Zeige den Titel in der Admin-Übersicht
    search_fields = ('title',)  # Ermögliche die Suche nach Titeln
