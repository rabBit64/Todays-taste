from django.shortcuts import render, redirect
from .models import Article, Comment, Product, ProductImages
from .forms import ArticleForm , CommentForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import User
from django.core.paginator import Paginator

# Create your views here.



def init(request):
    return redirect('articles:index')




def index(request):
    articles = Article.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    per_page = 9
    paginator = Paginator(articles, per_page)
    page_obj = paginator.get_page(page)
    page_num = paginator.num_pages

    if request.user.is_authenticated:
        nickname = request.user.nickname
        context = {
            'articles' : page_obj,
            'nickname' : nickname,
            'page_num': page_num,
        }
        return render(request, 'articles/index.html', context)
    else:
        context = {
            'articles' : page_obj,
            'page_num': page_num,
        }
    return render(request, 'articles/index.html', context)




def product(request):
    products = Product.objects.all()
    page = request.GET.get('page', '1')
    per_page = 9
    paginator = Paginator(products, per_page)
    page_obj = paginator.get_page(page)
    page_num = paginator.num_pages
    if request.user.is_authenticated:
        nickname = request.user.nickname
        context = {
            'products' : page_obj,
            'nickname' : nickname,
            'page_num': page_num,
        }
        return render(request, 'articles/product.html', context)
    else:
        context = {
            'products' : page_obj,
            'page_num': page_num,
        }
    return render(request, 'articles/product.html', context)




@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        article_model = Article(user=user,title=title,content=content,image=image)
        article_model.save()

        form = ArticleForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        article_model = Article(user=user,title=title,content=content,image=image)
        article_model.save()



        form = ArticleForm()
    context = {
        'form' : form,
        'article_model' : article_model
    }
    return render(request, 'articles/create.html',context)



#팔로우 추가
from django.contrib.auth import get_user_model

def detail(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(comments, per_page)
    page_obj = paginator.get_page(page)
    page_num = paginator.num_pages


    User = get_user_model()
    # person = User.objects.get(username=username)

    # 조회수
    article.view_count += 1
    article.save()
    if request.user.is_authenticated:
        nickname = request.user.nickname
        context = {
            'article': article,
            'comment_form' : comment_form,
            'comments' : page_obj,
            'page_num ' : page_num ,
            'nickname' : nickname,
        }
    else:
         context = {
            'article': article,
            'comment_form' : comment_form,
            'comments' : page_obj,
            'page_num ' : page_num ,
        }
    return render(request,'articles/detail.html',context)




@login_required
def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form
    }
    return render(request,'articles/update.html',context)




@login_required
def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')




@login_required
def create_comment(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request,'articles/detail.html',context)




@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)




@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')

@login_required
def scrap(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if article.scrap.filter(pk=request.user.pk).exists():
        article.scrap.remove(request.user)
    else:
        article.scrap.add(request.user)
    return redirect('articles:index')




def search(request):
    query = request.GET.get('q', '')
    if query:
        search = Article.objects.filter(
            Q(title__icontains=query)|
            Q(user__username__exact=query)
        )
    else:
        search = Article.objects.all()[::-1]
    context = {
        'articles' : search
    }
    print()
    return render(request, 'articles/index.html', context)


def category(request,subject):
    products = Product.objects.filter(category__contains=subject)
    page = request.GET.get('page', '1')
    per_page = 9
    paginator = Paginator(products, per_page)
    page_obj = paginator.get_page(page)
    page_num = paginator.num_pages
    context = {
        'products' : page_obj,
        'subject' : subject,
        'page_num' : page_num,
    }
    return render(request, 'articles/category.html', context)

#관리자 상품 업로드
# def addProduct(request):
#     user = request.user
#     if request.method=='POST':
#         data = request.POST
#         images = request.FILES.getlist('main_image')

#     for image in images:
#         product_image = Product.objects.create(
#             main_image=image,
#         )

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()

#             # images
#             for image in request.FILES.getlist('images'):
#                 photo = ProductImages(product=product, photo=image)
#                 photo.save()
#             return redirect('product_detail', pk=product.pk)
#     else:
#         form = ProductForm()
#     return render(request, 'articles/product_create.html', {'form': form})