from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)
