from django.contrib.auth.models import User
from rest_framework import serializers
from fsh.apps.snippet.models import Snippet, SnippetLike, SnippetComment #, LANGUAGE_CHOICES, STYLE_CHOICES

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
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    likes = SnippetLikeSerializer(many=True, read_only=True)
    comments = SnippetCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'user', 'title', 'source', 'linenos', 'language', 'style', 'highlight', 'likes', 'comments']
