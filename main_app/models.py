from django.db import models


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

    url = models.URLField(
        'Ссылка на вакансию',
        unique=True
    )
    name = models.CharField('Название', max_length=250)
    company = models.CharField('Компания', max_length=250)
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
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Список вакансий'
        ordering = ['-created_date', ]
