from django.contrib.auth.models import User
from rest_framework import serializers
from fsh.apps.snippet.models import Snippet, SnippetLike, SnippetComment, SnippetOfDay


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class UserSerializerSmall(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class SnippetLikeSerializer(serializers.ModelSerializer):
    user = UserSerializerSmall(read_only=True)

    class Meta:
        model = SnippetLike
        fields = ['id', 'user', 'liked_at']


class SnippetCommentSerializer(serializers.ModelSerializer):
    user = UserSerializerSmall(read_only=True)

    class Meta:
        model = SnippetComment
        fields = ['user', 'created_at', 'text', 'snippet']


class SnippetSerializer(serializers.ModelSerializer):
    user = UserSerializerSmall(read_only=True)
    highlighted = serializers.CharField(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'user', 'title', 'language', 'highlighted', 'count_likes', 'count_comments']


class SnippetOfDaySerializer(serializers.ModelSerializer):

    snippet = SnippetSerializer(read_only=True)

    class Meta:
        model = SnippetOfDay
        fields = ['id', 'day', 'snippet']
