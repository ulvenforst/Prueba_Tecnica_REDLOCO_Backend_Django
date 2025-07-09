from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Character
from ..forms import CharacterForm

class CharacterListView(ListView):
    model = Character
    template_name = "characters/character_list_crud.html"
    context_object_name = "characters"

class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character-crud-list")

class CharacterUpdateView(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character-crud-list")

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "characters/character_confirm_delete.html"
    success_url = reverse_lazy("character-crud-list")

