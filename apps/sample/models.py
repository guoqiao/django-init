# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models

class Setting(models.Model):
    key    = models.CharField(max_length=64,unique=True)
    value  = models.CharField(max_length=512)
    helps  = models.TextField(max_length=1024,blank=True,null=True)

# main model name
M = Setting
