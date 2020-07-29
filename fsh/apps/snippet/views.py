from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SnippetSerializer, UserSerializer, SnippetCommentSerializer, SnippetOfDaySerializer
from fsh.apps.snippet.models import Snippet, SnippetComment, SnippetOfDay


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

    @action(detail=False)
    def today(self, request, *args, **kwargs):
        snippet = SnippetOfDay.objects.first()

        serializer = self.serializer_class(snippet.snippet)
        serializer.data

        return Response(serializer.data)


class SnippetCommentViewSet(viewsets.ModelViewSet):
    queryset = SnippetComment.objects.all()
    serializer_class = SnippetCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SnippetOfDaySerializerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SnippetOfDay.objects.all()
    serializer_class = SnippetOfDaySerializer

    @action(detail=False)
    def last(self, request, *args, **kwargs):
        snippet = SnippetOfDay.objects.first()
        return Response(snippet)
