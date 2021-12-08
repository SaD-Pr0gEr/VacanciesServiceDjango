from django.urls import path
from main_app.views import main_page, vacancies

app_name = 'main_app'

urlpatterns = [
    path('', main_page, name='home'),
    path('vacancies/', vacancies, name='vacancies'),
]
