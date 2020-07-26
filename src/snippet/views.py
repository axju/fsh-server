from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Snippet, SnippetLike


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
    fields = ['title', 'language', 'source', 'description']

    def form_valid(self, form):
        snippet = form.save(commit=False)
        snippet.user = self.request.user
        return super(SnippetCreateView, self).form_valid(form)


class SnippetDetailView(DetailView):
    model = Snippet


class SnippetLikeAction(View):

    def dispatch(self, request, *args, **kwargs):
        self.object = Snippet.objects.get(pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        SnippetLike.objects.get_or_create(user=self.request.user, snippet=self.object)
        url = self.request.GET.get('next') or reverse_lazy('snippet:detail', args=[self.object.pk])
        return HttpResponseRedirect(url)
