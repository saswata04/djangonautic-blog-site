from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, id):
    # return HttpResponse(slug)
    article = Article.objects.get(id=id)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def article_edit(request, id):
    # return HttpResponse('Edit page')
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EditArticle(request.POST, request.FILES)
        if form.is_valid():
            article.title = request.POST.get('title')
            article.body = request.POST.get('body')
            # article.slug = request.POST.get('slug')
            # print(request.FILES.get('thumb'))
            if request.FILES.get('thumb') == None:
                pass
            else:
                article.thumb = request.FILES.get('thumb')
            article.author = request.user
            article.save()
            return redirect('articles:list')
    else:
        data_dict = {'title': article.title, 'body': article.body, 'thumb': article.thumb.url}
        form = forms.EditArticle(data_dict)
    return render(request, 'articles/article_edit.html', {'form': form, 'article': article})

def article_delete(request, id):
    # return HttpResponse('Delete page')
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        # print(request.POST.get('option')=='Yes')
        if request.POST.get('option') == 'Yes':
            article.delete()
            return redirect('articles:list')
        else:
            # return redirect(f'/articles/{id}/')
            return redirect('articles:detail', id)
    return render(request, 'articles/article_delete.html', {'article': article})
