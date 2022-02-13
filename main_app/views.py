from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from loguru import logger
from main_app.forms import HelpForm
from main_app.models import Vacancy, ProgramLanguage, Cities
from main_app.tasks import help_send


def main_page(request):
    """Главная страница"""

    last_created_vacancies = Vacancy.objects.all()[:6]
    context = {
        'title': "Home",
        "last_created": last_created_vacancies
    }
    return render(
        request,
        'main_app/index.html',
        context=context
    )


def vacancies(request):
    """Страница для вакансий"""

    if request.method == "POST":
        help_form = HelpForm(request.POST)
        if help_form.is_valid():
            name = help_form.cleaned_data['name']
            email = help_form.cleaned_data['email']
            text = help_form.cleaned_data['text']
            help_send.delay(name, email, text)
            messages.success(request, 'Заявка отправлена успешно!')
            return redirect("main_app:vacancies")
    else:
        help_form = HelpForm()
    cities = Cities.objects.all()
    langs = ProgramLanguage.objects.all()
    get_city = request.GET.get('city')
    get_lang = request.GET.get('lang')
    filters = {}
    if get_city or get_lang:
        if get_city:
            check_city = Cities.objects.filter(slug=get_city).first()
            if check_city:
                filters['city'] = check_city
        if get_lang:
            check_lang = ProgramLanguage.objects.filter(slug=get_lang).first()
            if check_lang:
                filters['language'] = check_lang
    if filters:
        vacancies_list = Vacancy.objects.prefetch_related("city", "language").filter(**filters).all()
    else:
        vacancies_list = Vacancy.objects.prefetch_related("city", "language").all()
    page = request.GET.get("page", 1)
    try:
        new_page = int(page)
    except ValueError:
        logger.warning("value error(str) with pagination page number")
        new_page = 1
    paginator = Paginator(vacancies_list, settings.PAGINATION_CONTENT_LENGTH)
    get_obj = paginator.get_page(int(new_page))
    context = {
        "title": "Вакансии",
        'vacancies': get_obj,
        "cities": cities,
        "langs": langs,
        "filter_city": get_city if get_city else None,
        "filter_lang": get_lang if get_lang else None,
        'help_form': help_form
    }
    return render(
        request,
        'main_app/vacancies.html',
        context=context
    )
