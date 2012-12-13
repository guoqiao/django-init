# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Snippet(models.Model):
    title = models.CharField(max_length=128)
    code = models.TextField()
    desc = models.TextField()
    user = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

admin.site.register(Snippet)
