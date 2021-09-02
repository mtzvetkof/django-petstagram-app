from django.urls import path

from petstagram.accounts.views import login_user, logout_user, register_user

urlpatterns = (
    path('login/', login_user, name='log in'),
    path('logout/', logout_user, name='log out'),
    path('register/', register_user, name='register'),
)