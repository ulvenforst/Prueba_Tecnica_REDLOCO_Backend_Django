from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..services.rick_and_morty_api import fetch_characters
from ..models import Character

@csrf_exempt  
def select_characters_view(request):
    page = int(request.GET.get("page", 1))
    data = fetch_characters(page=page)
    characters = data.get("results", []) if data else []
    info = data.get("info", {}) if data else {}


    if request.method == 'POST':
        selected_ids = request.POST.getlist('character_ids')
        next_page = request.POST.get("next_page")
        if selected_ids:
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
        # Si se hizo clic en “Guardar y siguiente”
        if next_page:
            return redirect(f"{request.path}?page={int(page) + 1}")
        return redirect(f"{request.path}?page={page}")

    return render(request, 'characters/character_list.html', {
        "characters": characters,
        "page": page,
        "has_next": info.get("next") is not None,
        "has_prev": info.get("prev") is not None,
    })


