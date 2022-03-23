from django.shortcuts import render, get_object_or_404
from django.views import View
from taggit.models import Tag

from .models import Article
from django.views.generic import TemplateView, ListView, DetailView


class ArticleView(ListView):
    template_name = 'article/article.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Adding a QuerySet of all the articles
        context['article_list'] = self.get_queryset()
        context['tags'] = Article.tags.most_common()
        return context

    def get_queryset(self):
        if self.kwargs:
            tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
            return Article.objects.filter(tags=tag)
        return Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article

    def get_queryset(self):
        qs = super(ArticleDetailView, self).get_queryset()
        return qs.filter(slug=self.kwargs['slug'])
