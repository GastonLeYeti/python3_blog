from django.http import Http404
from django.shortcuts import render
from blog.models import Article

def home(request):
    return render(request, 'blog/home.html')
  
  
def view_article(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/article.html', {'article': article})
  
  
  
def list_articles(request):
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/articles.html', {'derniers_articles': articles})
  