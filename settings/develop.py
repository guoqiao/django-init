#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from base import *

import logging
FMT = '%(asctime)s - %(levelname)s - %(message)s'
#CRITICAL ERROR WARNING INFO DEBUG
logging.basicConfig(level=logging.DEBUG, format=FMT)

DEBUG = True
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MIDDLEWARE_CLASSES += ()   # Add extra classes here
INSTALLED_APPS += ()       # Add extra apps here
