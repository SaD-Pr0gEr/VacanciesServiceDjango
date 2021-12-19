from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Cities, ProgramLanguage

User = get_user_model()


class LoginForm(forms.Form):
    """Форма для входа"""

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
    """Форма для регистрации"""

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


class UserUpdateForm(forms.ModelForm):
    """Форма для обновления профиля юзера"""

    city = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        to_field_name="slug",
        required=False,
        label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=ProgramLanguage.objects.all(),
        to_field_name="slug",
        required=False,
        label='Язык программирования'
    )
    subscribed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput,
        label='Подписка на рассылку'                              
    )
    password1 = forms.CharField(
        label='',
        max_length=300,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False
    )
    password2 = forms.CharField(
        label='',
        max_length=300,
        widget=forms.PasswordInput(attrs={"autocomplete": "false"}),
        required=False
    )

    class Meta:
        model = User
        fields = ('city', 'language', 'subscribed', 'password1', 'password2')
