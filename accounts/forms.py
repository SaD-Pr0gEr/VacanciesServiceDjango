from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': "email", "class": 'form-control'})
    )
    password = forms.CharField(
        max_length=150,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': "Пароль*", "class": 'form-control'})
    )


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label='',
        max_length=300,
        widget=forms.PasswordInput(attrs={'placeholder': "Пароль"})
    )
    password2 = forms.CharField(
        label='',
        max_length=300,
        widget=forms.PasswordInput(attrs={'placeholder': "Пароль ещё раз"})
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email*"})
        }
