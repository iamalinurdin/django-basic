from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    return render(request, 'article/index.html', {
        'articles': Article.objects.all()
    })

def show(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'article/read.html', {'article': article})
    # return HttpResponse(id)

@login_required(login_url = '/account/login')
def create(request):
    return render(request, 'article/create.html')