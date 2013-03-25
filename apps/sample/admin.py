# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models as m

class SettingAdmin(admin.ModelAdmin):
    list_display = ('key','value','helps')

admin.site.register(m.Setting,SettingAdmin)

