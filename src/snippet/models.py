from django.conf import settings
from django.db import models


class Snippet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    title = models.CharField(max_length=100)
    description = models.TextField()
    source = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}'.format(self.title)
