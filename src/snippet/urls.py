from django.urls import path, include
from .views import SnippetListView, SnippetCreateView


app_name = 'snippet'

urlpatterns = [
    path('', SnippetListView.as_view(), name='index'),
    path('create/', SnippetCreateView.as_view(), name='create'),
]
