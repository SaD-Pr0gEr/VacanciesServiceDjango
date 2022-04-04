from django.conf import settings
from django.db import models


class Company(models.Model):
    """Модель компаний"""

    name = models.CharField("Название компании", max_length=120)
    title = models.TextField("Описание компании")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Создатель",
        related_name="author_companies",
        on_delete=models.CASCADE
    )
    logo = models.ImageField(
        "Логотип",
        upload_to="company_photos/",
        null=True,
        blank=True,
        help_text="Опционально"
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Model Company: {self.name}"

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ["-pk", ]


class Cities(models.Model):
    """Модель городов"""

    name = models.CharField(
        'Название',
        max_length=220,
        unique=True
    )
    slug = models.SlugField('URL', unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Список городов'
        ordering = ['name', ]


class ProgramLanguage(models.Model):
    """Модель языков программирования"""

    name = models.CharField(
        'Название',
        max_length=220,
        unique=True
    )
    slug = models.SlugField('URL', unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Список языков программирования'
        ordering = ['name', ]


class Vacancy(models.Model):
    """Модель вакансий"""

    author = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="company_vacancies",
        verbose_name="Компания"
    )
    name = models.CharField('Название', max_length=250)
    description = models.TextField("Описание")
    city = models.ForeignKey(
        Cities,
        related_name='city_vacancies',
        verbose_name='Город',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    language = models.ForeignKey(
        ProgramLanguage,
        related_name='language_vacancies',
        verbose_name='Язык программирования',
        on_delete=models.CASCADE
    )
    phone_contact = models.CharField(
        "Номер связи",
        max_length=120
    )
    email_contact = models.CharField(
        "Email связи",
        max_length=120
    )
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Список вакансий'
        ordering = ['-created_date', ]
