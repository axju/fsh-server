from django.urls import path, include
from rest_framework import routers
from fsh.apps.snippet.views import SnippetViewSet, SnippetCommentViewSet, SnippetOfDaySerializerViewSet


router = routers.SimpleRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'snippets_of_day', SnippetOfDaySerializerViewSet)
router.register(r'comments', SnippetCommentViewSet)


app_name = 'snippet'

urlpatterns = [
    path('', include(router.urls)),
]
