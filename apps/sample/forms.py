# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from . import models as m

class Form(forms.ModelForm):
    class Meta:
        model = m.M

NewForm = Form
EditForm = Form
DetailForm = Form
