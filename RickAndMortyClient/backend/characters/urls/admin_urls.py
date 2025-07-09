from django.urls import path
from ..views import admin_views

urlpatterns = [
    path('select/', admin_views.select_characters_view, name='character-select'),
]

