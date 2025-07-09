from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "api_id", "name", "status", "species",
            "gender", "origin_name", "image"
        ]
        widgets = {
            "image": forms.URLInput(attrs={"size": 40}),
        }

