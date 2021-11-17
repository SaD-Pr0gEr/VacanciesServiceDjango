from django.urls import path
from main_app.views import hello


urlpatterns = [
    path('', hello, name='home'),
]
