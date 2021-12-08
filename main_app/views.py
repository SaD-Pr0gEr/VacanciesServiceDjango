from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from main_app.models import Vacancy, ProgramLanguage, Cities


def hello(request):
    context = {
        'title': "Home"
    }
    return render(
        request,
        'main_app/index.html',
        context=context
    )


def vacancies(request):
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
        new_page = 1
    paginator = Paginator(vacancies_list, settings.PAGINATION_CONTENT_LENGTH)
    get_obj = paginator.get_page(int(new_page))
    context = {
        "title": "Вакансии",
        'vacancies': get_obj,
        "cities": cities,
        "langs": langs,
        "current_url": reverse('main_app:vacancies'),
        "filter_city": get_city if get_city else None,
        "filter_lang": get_lang if get_lang else None
    }
    return render(
        request,
        'main_app/vacancies.html',
        context=context
    )
