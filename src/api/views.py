from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SnippetSerializer, UserSerializer, SnippetCommentSerializer
from snippet.models import Snippet, SnippetComment


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        snippet = self.get_object()
        _, created = snippet.likes.get_or_create(user=request.user)
        if created:
            return Response({'status': 'like snippet'})
        return Response({'status': 'snippet already liked'})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SnippetCommentViewSet(viewsets.ModelViewSet):
    queryset = SnippetComment.objects.all()
    serializer_class = SnippetCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
