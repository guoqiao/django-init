# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def index(request):
    ctx = {}
    return render(request, 'main/index.html', ctx)

