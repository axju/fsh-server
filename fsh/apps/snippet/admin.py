from django.contrib import admin

from .models import Snippet, SnippetOfDay

class SnippetAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'source', 'language', 'style', 'linenos']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(SnippetOfDay)
