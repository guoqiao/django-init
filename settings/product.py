#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_ROOT = '/var/www/%s/static/' % PROJECT_NAME
MEDIA_ROOT  = '/var/www/%s/media/'  % PROJECT_NAME

HOST = 'http://iot.insigma.com.cn'

STATIC_URL = '%s/%s/static/' % (HOST,PROJECT_NAME)
MEDIA_URL  = '%s/%s/media/' %  (HOST,PROJECT_NAME)

MIDDLEWARE_CLASSES += ()   # Add extra classes here
INSTALLED_APPS += ()       # Add extra a/pps here
