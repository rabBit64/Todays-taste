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
    class Meta:
        username = forms.CharField(label='아이디')
        email = forms.EmailField(label='이메일')
        
        model = get_user_model()
        fields = ('username','password1','password2')

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(label='아이디')
    email = forms.EmailField(label='이메일')

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email')
        