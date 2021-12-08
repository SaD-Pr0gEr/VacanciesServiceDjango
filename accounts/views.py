from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, SignUpForm
from main_app.tasks import hello_sender

User = get_user_model()


def login_page(request, ):
    """Страница для логина"""

    if request.user.is_authenticated:
        return redirect('main_app:home')
    if request.user.is_anonymous and request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_data = login_form.cleaned_data
            email = user_data['email']
            password = user_data['password']
            check_email = User.objects.filter(email=email).first()
            if check_email:
                auth_user = authenticate(request, email=email, password=password)
                if auth_user:
                    login(request, auth_user)
                    messages.success(request, 'Вы успешно вошли в систему!')
                    return redirect('main_app:home')
                else:
                    messages.error(request, 'Логин или пароль неправильные')
            else:
                messages.error(request, 'Пользователь с таким email не существует!')
    else:
        login_form = LoginForm()
    context = {
        'title': "Вход",
        'login_form': login_form,
    }
    return render(
        request,
        'accounts/login_page.html',
        context=context
    )


def signup_page(request):
    """Страница для регистрации"""

    if request.user.is_authenticated:
        return redirect('main_app:home')
    if request.user.is_anonymous and request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_data = signup_form.cleaned_data
            email = user_data['email']
            check_email = User.objects.filter(email=email).first()
            if not check_email:
                password = user_data['password1']
                user = signup_form.save(commit=False)
                user.is_active = True
                user.set_password(password)
                user.save()
                hello_sender.delay(email)
                messages.success(request, 'Вы успешно зарегистрировались! Теперь войдите в систему')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Пользователь с таким email уже существует!')
    else:
        signup_form = SignUpForm()
    context = {
        'title': "Регистрация",
        'signup_form': signup_form,
    }
    return render(
        request,
        'accounts/signup_page.html',
        context=context
    )


@login_required(login_url='accounts:login')
def logout_page(request):
    """Страница для выхода"""

    if request.method == "GET":
        logout(request)
        messages.success(request, 'Вы успешно вышли')
    else:
        messages.info(request, 'Метод POST не разрешен')
    return redirect('main_app:home')


@login_required(login_url='accounts:login')
def profile(request):
    """Страница для просмотра профиля"""

    context = {
        'title': "Мой профиль",
    }
    return render(
        request,
        'accounts/profile.html',
        context=context
    )
