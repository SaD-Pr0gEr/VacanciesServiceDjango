from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from loguru import logger

from main_app.email_senders import help_sender
from main_app.forms import HelpForm, VacancyForm, CompanyForm
from main_app.models import Vacancy, ProgramLanguage, Cities, Company
# from main_app.tasks import help_send


def main_page(request: WSGIRequest):
    """Главная страница"""

    last_created_vacancies = Vacancy.objects.all()[:6]
    help_form = HelpForm()
    context = {
        "title": "Home",
        "last_created": last_created_vacancies,
        "help_form": help_form
    }
    return render(
        request,
        "main_app/index.html",
        context=context
    )


@login_required(login_url="accounts:login")
def help_view(request: WSGIRequest):
    """Обработчик формы помощи"""

    if not request.method == "POST":
        messages.info(request, "Разрешен только POST метод")
        return redirect("main_app:home")
    help_form = HelpForm(request.POST)
    if help_form.is_valid():
        name = help_form.cleaned_data["name"]
        email = help_form.cleaned_data["email"]
        text = help_form.cleaned_data["text"]
        # help_send.delay(name, email, text)
        if help_sender(name, email, text):
            messages.success(request, "Заявка отправлена успешно!")
        else:
            messages.error(request, "Не удалось отправить! Попробуйте позже!")
    else:
        for errors in help_form.errors:
            for error in errors:
                messages.error(request, error)
    return redirect("main_app:vacancies")


@login_required(login_url='accounts:login')
def vacancies(request: WSGIRequest):
    """Страница для вакансий"""

    help_form = HelpForm()
    cities = Cities.objects.all()
    langs = ProgramLanguage.objects.all()
    get_city = request.GET.get("city")
    get_lang = request.GET.get("lang")
    filters = {}
    if get_city or get_lang:
        if get_city:
            check_city = Cities.objects.filter(slug=get_city).first()
            if check_city:
                filters["city"] = check_city
        if get_lang:
            check_lang = ProgramLanguage.objects.filter(slug=get_lang).first()
            if check_lang:
                filters["language"] = check_lang
    if filters:
        vacancies_list = Vacancy.objects.prefetch_related("city", "language").filter(**filters).all()
    else:
        vacancies_list = Vacancy.objects.prefetch_related("city", "language").all()
    page = request.GET.get("page", 1)
    try:
        new_page = int(page)
    except ValueError:
        logger.add(settings.BASE_DIR / 'logs/all/all.log', level="INFO")
        logger.warning("value error(str) with pagination page number")
        new_page = 1
    paginator = Paginator(vacancies_list, settings.PAGINATION_CONTENT_LENGTH)
    get_obj = paginator.get_page(int(new_page))
    context = {
        "title": "Вакансии",
        'vacancies': get_obj,
        "cities": cities,
        "langs": langs,
        "filter_city": get_city,
        "filter_lang": get_lang,
        "help_form": help_form
    }
    return render(
        request,
        "main_app/vacancies.html",
        context=context
    )


@login_required(login_url='accounts:login')
def vacancy_page(request: WSGIRequest, pk: int):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    help_form = HelpForm()
    context = {
        "title": vacancy.name,
        "vacancy": vacancy,
        "help_form": help_form
    }
    return render(
        request,
        "main_app/vacancy_page.html",
        context=context
    )


@login_required(login_url='accounts:login')
def company_info(request: WSGIRequest, pk):
    company = get_object_or_404(Company, pk=pk)
    help_form = HelpForm()
    context = {
        "title": company.name,
        "company": company,
        "help_form": help_form
    }
    return render(
        request,
        "main_app/company_info.html",
        context=context
    )


@login_required(login_url="accounts:login")
def create_vacancy(request: WSGIRequest):
    if not request.user.author_companies.first():
        messages.info(request, "Сначала создайте компанию")
        return redirect("main_app:create_company")
    if request.method == "POST":
        create_form = VacancyForm(request.POST)
        if create_form.is_valid():
            save = create_form.save(commit=False)
            save.author = request.user.author_companies.first()
            save.save()
            messages.success(request, "Успешно добавлено!")
            return redirect("main_app:home")
    else:
        create_form = VacancyForm()
    help_form = HelpForm()
    context = {
        "title": "Добавить вакансию",
        "help_form": help_form,
        "create_form": create_form
    }
    return render(
        request,
        "main_app/create_vacancy.html",
        context=context
    )


@login_required(login_url="accounts:login")
def create_company(request: WSGIRequest):
    if request.user.author_companies.first():
        messages.info(request, "У вас уже есть компания!")
        return redirect("main_app:home")
    if request.method == "POST":
        create_form = CompanyForm(request.POST, request.FILES)
        if create_form.is_valid():
            save = create_form.save(commit=False)
            save.owner = request.user
            save.save()
            messages.success(request, "Успешно добавлено!")
            return redirect("main_app:home")
    else:
        create_form = CompanyForm()
    help_form = HelpForm()
    context = {
        "title": "Добавить вакансию",
        "help_form": help_form,
        "create_form": create_form
    }
    return render(
        request,
        "main_app/create_company.html",
        context=context
    )
