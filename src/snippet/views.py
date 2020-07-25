from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Snippet


class IndexView(TemplateView):
    template_name = 'snippet/index.html'


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippet/snippet_list.html'
    paginate_by = 50


class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    template_name = 'snippet/snippet_create.html'
    success_url = reverse_lazy('snippet:index')
    fields = ['title', 'description', 'source']

    def form_valid(self, form):
        snippet = form.save(commit=False)
        snippet.user = self.request.user
        return super(SnippetCreateView, self).form_valid(form)
