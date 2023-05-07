from django import forms
from .models import Article,Comment,Product

    
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

 

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='제목', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 700px;','placeholder': '제목',}))
    content = forms.CharField(label='리뷰', label_suffix='', widget=forms.Textarea(
        attrs={'class': 'form-control','style': 'width: 700px; height: 150px;', 'placeholder': '리뷰를 작성해서 취향을 공유해주세요 :)',}))

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['review_product'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return "%s" % obj.product_name
    
    class Meta:
        model = Article
        fields = ('title','image','content','review_product')
        # fields = ('title','image','content','star_ranking')
    
   

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


