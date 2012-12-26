# -*- coding: utf-8 -*-

import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import mail
from django.conf import settings
from django.shortcuts import render as r
#from django.shortcuts import redirect

APP_NAME = os.path.split(os.path.dirname(__file__))[-1]

def _render(request,tmpl,*args,**kwargs):
    return r(request,'%s/%s' % (APP_NAME,tmpl),*args,**kwargs)

def index(request):
    ctx = {}
    #mail.mail_admins('mailer test','hey man')
    #mail.send_mail('Subject here', 'Here is the message.', 'spig@insigma.com.cn',['guoqiao@gmail.com'], fail_silently=False)
    email = mail.EmailMessage(
            'Hello',# subject
            'Body goes here',# body
            'spig@insigma.com.cn',# from
            ['guoqiao@gmail.com',],# to
            ['guoqiao@insigma.com.cn'],# bcc
            headers = {'Reply-To': 'huxiaomao@insigma.com.cn'},
            )
    x = os.path.join(settings.PROJECT_ROOT,'README.md')
    y = os.path.join(settings.PROJECT_ROOT,'manage.py')
    email.attach_file(x)
    email.attach_file(y)
    email.send()

    return _render(request, 'index.html', ctx)

