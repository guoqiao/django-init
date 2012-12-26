#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from base import *

DEBUG = True
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MIDDLEWARE_CLASSES += ()   # Add extra classes here
INSTALLED_APPS += ()       # Add extra apps here
