from rest_framework.routers import DefaultRouter
from characters.views.api_views import CharacterViewSet, fetch_characters_view, save_characters_view
from django.urls import path

router = DefaultRouter()
router.register(r'', CharacterViewSet, basename='character')

urlpatterns = [
    path('fetch/', fetch_characters_view, name='api-fetch-characters'),
    path('save/', save_characters_view, name='api-save-characters'),
]

urlpatterns += router.urls
