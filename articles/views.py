from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def init(request):
    return redirect('articles:index')



def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

