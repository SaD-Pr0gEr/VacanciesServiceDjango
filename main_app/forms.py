from django import forms


class HelpForm(forms.Form):
    """Форма для помощи"""

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "input", 'placeholder': "Имя*"},
        ),
        label=''
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': "input", 'placeholder': "Email*"}
        ),
        label=''
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "input",
                'placeholder': "Текст",
                'cols': 25,
                'rows': 5
            }
        ),
        label='',
        max_length=500
    )
