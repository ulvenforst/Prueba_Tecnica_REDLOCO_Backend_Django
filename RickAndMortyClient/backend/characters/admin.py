from django.contrib import admin
from .models import Character

# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_id', 'species', 'status']
    search_fields = ['name', 'api_id']
