from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content','image')

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
    class Meta:
        model = Comment
        fields = ('content',)