# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import os
from django.db import models
from path import path

# abs path of this file
FILE = path(os.path.abspath(__file__))
# abs path of this dir
APP_ROOT = FILE.parent
# name of this app
APP_NAME = APP_ROOT.name


class Setting(models.Model):
    key    = models.CharField(max_length=64,unique=True)
    value  = models.CharField(max_length=512)
    helps  = models.TextField(max_length=1024,blank=True,null=True)

# main model name
M = Setting
