from django import forms
from .models import Article,Comment,Product
from django.contrib import admin


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='제목', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 360px;','placeholder': '제목',}))
    content = forms.CharField(label='리뷰', label_suffix='', widget=forms.Textarea(
        attrs={'class': 'form-control','style': 'width: 360px; height: 150px;', 'placeholder': '리뷰 작성',}))
    # image = forms.ImageField(
    #     widget = forms.FileInput(
    #         attrs = {"id" : "image_field" , 
    #                 'style' : "height: 100px; width : 360px;", 
    #                 }
    #         )
    # )
    class Meta:
        model = Article
        fields = ('title','image','content',)

    # title = forms.CharField(
    #     label='제목',
    # )
    # content = forms.CharField(
    #     label = '내용',
    # )

    # image = forms.ImageField(
    #     label = '이미지'
    # )
    # class Meta:
    #     model = Article
    #     fields = ('title','content','image')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 100%; display: inline-flex; border:0px;',
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)
        label_suffix = ''


class ProductForm(forms.ModelForm):
    CATEGORIES= (
        ('가구', '가구'), #가구
        ('식품', '식품'), #식품
        ('생필품', '생필품'), #생필품
        ('생활용품', '생활용품'), #생활용품
        ('디지털', '디지털'), #디지털
        ('데코', '데코'), #데코
        ('반려동물', '반려동물'), #반려동물
        ('캠핑', '캠핑'), #캠핑
        ('조명', '조명'), #조명
    )

    category = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-select mt-2',
            }
        ),
        choices=CATEGORIES)

    class Meta:
        model = Product
        fields = ('product_name', 'price', 'category', 'content',)

    # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # product_name = forms.CharField()
    # price = forms.IntegerField()
    # category = forms.CharField()
    # content = forms.CharField(widget=forms.Textarea)
    # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


