from django import forms

from main_app.models import Vacancy


class HelpForm(forms.Form):
    """Форма для помощи"""

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "input col-6", "placeholder": "Имя*"},
        ),
        label=''
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "input col-6", "placeholder": "Email*"}
        ),
        label=""
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "input col-8",
                "placeholder": "Текст",
                "style": "resize: none;"
            }
        ),
        label='',
        max_length=500
    )
