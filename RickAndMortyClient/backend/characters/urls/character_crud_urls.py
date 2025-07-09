from django.urls import path
from ..views.character_crud_views import *

urlpatterns = [
    path('', CharacterListView.as_view(), name='character-crud-list'),
    path('create/', CharacterCreateView.as_view(), name='character-crud-create'),
    path('<int:pk>/edit/', CharacterUpdateView.as_view(), name='character-crud-edit'),
    path('<int:pk>/delete/', CharacterDeleteView.as_view(), name='character-crud-delete'),
]

