from django.db import models

class MarkdownPage(models.Model):
    title = models.CharField(max_length=200)  # Titel der Seite
    content = models.TextField()  # Markdown-Inhalt
    category = models.CharField(max_length=100)  # Kategorie: z.B. 'Application', 'Article'

    def __str__(self):
        return f"{self.title} - {self.category}"
