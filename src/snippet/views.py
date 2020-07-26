from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.forms.models import modelform_factory

from .models import Snippet, SnippetLike, SnippetComment


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

    def get_context_data(self, **kwargs):
        kwargs['comment_form'] = modelform_factory(SnippetComment, fields=['text'])
        return super().get_context_data(**kwargs)


class SnippetLikeAction(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.object = Snippet.objects.get(pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        SnippetLike.objects.get_or_create(user=self.request.user, snippet=self.object)
        url = self.request.GET.get('next') or reverse_lazy('snippet:detail', args=[self.object.pk])
        return HttpResponseRedirect(url)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = SnippetComment
    template_name = 'snippet/comment_create.html'
    fields = ['text']

    def dispatch(self, request, *args, **kwargs):
        self.snippet = Snippet.objects.get(pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('snippet:detail', args=[self.snippet.pk])

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.snippet = self.snippet
        comment.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)
