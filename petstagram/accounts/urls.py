from django.urls import path

from petstagram.accounts.views import login_user, logout_user, register_user, profile_details

urlpatterns = (
    path('login/', login_user, name='log in'),
    path('logout/', logout_user, name='log out'),
    path('register/', register_user, name='register'),
    path('profile/', profile_details, name='profile details'),
)