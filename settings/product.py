#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_ROOT = '/var/www/ship/static/'
MEDIA_ROOT  = '/var/www/ship/media/'

STATIC_URL = 'http://iot.insigma.com.cn/ship/static/'
MEDIA_URL  = 'http://iot.insigma.com.cn/ship/media/'

MIDDLEWARE_CLASSES += ()   # Add extra classes here
INSTALLED_APPS += ()       # Add extra a/pps here
