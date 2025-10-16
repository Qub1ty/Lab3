from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    
    qs = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': qs})

def article_detail(request, pk):
   
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})
