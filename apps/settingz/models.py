# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class SettingManager(models.Manager):

    def get_str(self,key):
        return super(SettingManager,self).get(key=key).value

    def get_int(self,key):
        return int(self.get_str(key))

class Setting(models.Model):
    key    = models.CharField(max_length=64,unique=True)
    value  = models.CharField(max_length=512)
    helps  = models.TextField(max_length=1024,blank=True,null=True)
    objects = SettingManager()

class SettingAdmin(admin.ModelAdmin):
    list_display = ('key','value','helps')

admin.site.register(Setting,SettingAdmin)

