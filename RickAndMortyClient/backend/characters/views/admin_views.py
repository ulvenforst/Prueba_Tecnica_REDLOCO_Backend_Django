from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..services.rick_and_morty_api import fetch_characters
from ..models import Character

@csrf_exempt  
def select_characters_view(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('character_ids')
        if selected_ids:
            data = fetch_characters()
            characters = data.get("results", []) if data else []
            for character in characters:
                if str(character["id"]) in selected_ids:
                    Character.objects.get_or_create(
                        api_id=character["id"],
                        defaults={
                            "name": character["name"],
                            "status": character["status"],
                            "species": character["species"],
                            "gender": character["gender"],
                            "origin_name": character["origin"]["name"],
                            "image": character["image"]
                        }
                    )
        return redirect('character-select') 

    data = fetch_characters()
    characters = data.get("results", []) if data else []
    return render(request, 'characters/character_list.html', {"characters": characters})

