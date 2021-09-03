from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from petstagram.accounts.forms import LoginForm, RegisterForm


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing')
