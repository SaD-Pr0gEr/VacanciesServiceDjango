from django.urls import path
from accounts.views import login_page, signup_page, logout_page, profile, user_update, delete_account

app_name = 'accounts'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logout_page, name='logout'),
    path("profile/", profile, name='profile'),
    path("update/", user_update, name='update_profile'),
    path("delete/", delete_account, name='delete_account'),
]
