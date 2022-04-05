from django.urls import path
from main_app.views import main_page, vacancies, vacancy_page, help_view, company_info, create_vacancy

app_name = 'main_app'

urlpatterns = [
    path('', main_page, name='home'),
    path('vacancies/', vacancies, name='vacancies'),
    path('vacancy/<int:pk>', vacancy_page, name='vacancy'),
    path('help/', help_view, name='help'),
    path('company/info/<int:pk>', company_info, name='company_info'),
]
