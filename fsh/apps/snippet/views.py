from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SnippetSerializer, SnippetCreateSerializer, UserSerializer, SnippetCommentSerializer, SnippetOfDaySerializer
from fsh.apps.snippet.models import Snippet, SnippetComment, SnippetOfDay
from .models import LANGUAGE_CHOICES, STYLE_CHOICES
from fsh import __version__


class InfoView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, format=None):
        return Response({'version': __version__, 'language': LANGUAGE_CHOICES, 'style': STYLE_CHOICES})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.action == 'create':
            return SnippetCreateSerializer
        return SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def like(self, request, *args, **kwargs):
        snippet = self.get_object()
        _, created = snippet.likes.get_or_create(user=request.user)
        return self.retrieve(request, pk=snippet.pk)

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
