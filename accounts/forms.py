from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디 입력',
                'style': 'width: 300px',
                'style': 'height: 50px',
            })
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 입력',
                'style': 'width: 300px',
                'style': 'height: 50px',
            })
    )

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(label='아이디', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 360px;','placeholder': '별명 (2~15자)','id':'user_id',}))
    username = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 170px;', 'placeholder': '이메일',}))
    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control placeholder-font','style': 'width: 360px;', 'placeholder': '비밀번호',}))
    password2 = forms.CharField(label='비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control placeholder-font', 'style': 'width: 360px;','placeholder': '비밀번호 확인',}))
    class Meta:
        username = forms.CharField(label='아이디')
        email = forms.EmailField(label='이메일')
        
        model = get_user_model()
        fields = ('nickname','username','password1','password2',)




class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(label='아이디')
    email = forms.EmailField(label='이메일')

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email')
        