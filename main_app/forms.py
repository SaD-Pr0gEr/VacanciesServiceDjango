from cProfile import label

from django import forms

from main_app.models import Vacancy, Company


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


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            "name", "description", "city",
            "language", "phone_contact", "email_contact",
            "billing_from", "billing_to", "experience",
            "work_type"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "city": forms.Select(attrs={"class": "form-select"}),
            "language": forms.Select(attrs={"class": "form-select"}),
            "phone_contact": forms.NumberInput(attrs={"class": "form-control"}),
            "email_contact": forms.TextInput(attrs={"class": "form-control"}),
            "billing_from": forms.NumberInput(attrs={"class": "form-control"}),
            "billing_to": forms.NumberInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "work_type": forms.Select(attrs={"class": "form-select"})
        }
        label = {
            "name": "Название",
            "description": "Описание",
            "city": "Город",
            "language": "Язык программирования",
            "phone_contact": "Контактный номер",
            "email_contact": "Контактный email",
            "billing_from": "Зарплата(от-) $",
            "billing_to": "Зарплата(до-) $",
            "experience": "Опыт работы",
            "work_type": "Формат работы",
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "title", "logo"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.Textarea(attrs={"class": "form-control"}),
            "logo": forms.FileInput(attrs={"class": "form-control"})
        }
