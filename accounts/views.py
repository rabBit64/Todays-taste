from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from articles.models import Article




def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            print(request.user)
            auth_login(request, form.get_user()) 
            return redirect('articles:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)




@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)




@login_required
def profile(request,pk):
    User_detail = get_user_model().objects.get(pk=pk)
    context = {
        'User_detail':User_detail,
    }
    return render(request,'accounts/profile.html',context)




@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: 
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request,'accounts/update.html', context)




@login_required
def delete(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect(request,'articles:index')




def profile(request,username):
    User = get_user_model()
    person = User.objects.get(username=username)
    articles = Article.objects.all()
    context = {
        'person':person,
        'articles' : articles,
    }
    return render(request,'accounts/profile.html',context)




# 게시글 작성 유저 팔로우 ajax
@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk) #article 유저
    me = request.user

    if you!=me:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed=False
        else:
            you.followers.add(me)
            is_followed=True
        context = {
            'is_followed':is_followed,
            # 'following_count':you.followings.count(),
            # 'followers_count':you.followers.count(),
        }
        return JsonResponse(context)
        # return redirect('articles:detail',user_pk)
    return redirect('articles:detail',user_pk,context)

