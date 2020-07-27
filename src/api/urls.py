from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, SnippetViewSet, SnippetCommentViewSet


router = routers.DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'comments', SnippetCommentViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
