from django.conf import settings
from django.db import models
import base64
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters import ImageFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    title = models.CharField(max_length=100)
    source = models.TextField()
    description = models.TextField(null=True, blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}'.format(self.title)

    def count_likes(self):
        return self.likes.count()

    def count_comments(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        formatter = ImageFormatter(style=self.style, line_numbers=self.linenos, font_size=15, image_format='PNG', image_pad=20)
        image_file = highlight(self.source, lexer, formatter)
        self.highlighted = base64.b64encode(image_file).decode()
        super(Snippet, self).save(*args, **kwargs)


class SnippetLike(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name='likes')


class SnippetComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']


class SnippetOfDay(models.Model):
    day = models.DateField(unique=True)
    snippet = models.OneToOneField(Snippet, on_delete=models.CASCADE)
