from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

# 1. Accueil (Home Page) - Route: /
def accueil(request):
    derniers_articles = Article.objects.order_by('-datecreation')[:3]
    return render(request, 'blog/accueil.html', {'articles': derniers_articles})

# 2. Blog Page - Route: /blog/
def blog_list(request):
    articles = Article.objects.order_by('-datecreation')
    return render(request, 'blog/blog_list.html', {'articles': articles})

# 3. Détails Article - Route: /blog/<int:pk>/
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

# 4. Modifier Article - Route: /blog/<int:pk>/modifier/
def article_modifier(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_modifier.html', {'form': form, 'article': article})

# 5. Supprimer Article - Route: /blog/<int:pk>/supprimer/
def article_supprimer(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('blog_list')
    return render(request, 'blog/article_supprimer.html', {'article': article})