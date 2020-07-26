from django.urls import path, include
from .views import SnippetListView, SnippetCreateView, SnippetDetailView, SnippetLikeAction, CommentCreateView


app_name = 'snippet'

urlpatterns = [
    path('', SnippetListView.as_view(), name='index'),
    path('create/', SnippetCreateView.as_view(), name='create'),
    path('<pk>/', SnippetDetailView.as_view(), name='detail'),
    path('<pk>/like', SnippetLikeAction.as_view(), name='like'),
    path('<pk>/comment', CommentCreateView.as_view(), name='comment'),
]
