from django.shortcuts import render
from .models import Article


# Create your views here.
def article_list(request):
    list_all_article = Article.objects.all()
    context = {
        'list_all_article': list_all_article
    }
    return render(request, 'articles/article_list.html', context)

