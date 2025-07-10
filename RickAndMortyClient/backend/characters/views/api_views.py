from rest_framework import viewsets
from characters.serializers import CharacterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from characters.services.rick_and_morty_api import fetch_characters
from rest_framework import status
from characters.models import Character

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

@api_view(['GET'])
def fetch_characters_view(request):
    data = fetch_characters()
    return Response(data.get("results", []) if data else [])

@api_view(['POST'])
def save_characters_view(request):
    print("Saving characters...")
    selected_ids = request.data.get('character_ids', [])
    if not selected_ids:
        return Response({'error': 'No character_ids provided'}, status=status.HTTP_400_BAD_REQUEST)

    data = fetch_characters()
    if not data:
        return Response({'error': 'Failed to fetch characters'}, status=status.HTTP_502_BAD_GATEWAY)

    saved = []
    for character in data.get("results", []):
        if character["id"] in selected_ids:
            print(f"{character['id']} - {character['name']}")
            obj, _ = Character.objects.get_or_create(
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
            saved.append(obj.api_id)

    return Response({'saved_ids': saved}, status=Status.HTTP_201_CREATED)
