# myapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import MarkdownPage
import markdown

def home(request):
    # Alle Markdown-Seiten abrufen
    all_pages = MarkdownPage.objects.all()
    return render(request, 'home.html', {'all_pages': all_pages})

def application_detail(request, app_id):
    app = get_object_or_404(MarkdownPage, id=app_id)
    app.content = markdown.markdown(app.content) 
    return render(request, 'application.html', {'app': app})

def article_detail(request, article_id):
    article = get_object_or_404(MarkdownPage, id=article_id)
    app.content = markdown.markdown(app.content) 
    return render(request, 'article.html', {'article': article})