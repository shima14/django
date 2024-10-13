# myapp/urls.py

from django.urls import path
from .views import home, application_detail, article_detail

urlpatterns = [
    path('', home, name='home'),  # URL für die Homepage
    path('applications/<int:app_id>/', application_detail, name='application_detail'),  # URL für Anwendung
    path('articles/<int:article_id>/', article_detail, name='article_detail'),  # URL für Artikel
]
