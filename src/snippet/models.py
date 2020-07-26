from pygments.lexers import get_all_lexers
from django.conf import settings
from django.db import models


class Snippet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    title = models.CharField(max_length=100)
    description = models.TextField()
    source = models.TextField()
    language = models.CharField(
        max_length=32,
        choices=[(item[1][0], item [0]) for item in get_all_lexers()],
        default='python',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}'.format(self.title)


class SnippetLike(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name='likes')


class SnippetComment(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
