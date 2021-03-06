# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect

def index(request):
    users = User.objects.all()
    return render(request, 'accounts/index.html', { 'users':users })

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering, you can now login.')
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signin.html', { 'form': form })


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, u'你已经成功退出.')
    return redirect('main:index')
