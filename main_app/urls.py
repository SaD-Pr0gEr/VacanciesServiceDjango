from django.urls import path
from main_app.views import hello, vacancies

app_name = 'main_app'

urlpatterns = [
    path('', hello, name='home'),
    path('vacancies/', vacancies, name='vacancies'),
]
