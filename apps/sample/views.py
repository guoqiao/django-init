# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from . import models as m
from . import forms  as f

# auto get app name and tmpl name
def auto_render(function):
    def wrapper(request, *args, **kwargs):
        output = function(request, *args, **kwargs)
        if not isinstance(output, dict):
            return output
        s = '%s/%s.html' % (m.APP_NAME,function.__name__)
        return render(request,s,output)
    return wrapper

# auto add namespace
def auto_redirect(url_name,**kwargs):
    s = '%s:%s' % (m.APP_NAME,url_name)
    return redirect(s,**kwargs)

@auto_render
def index(request):
    ctx = {}
    ctx['objs'] = m.M.objects.all()
    return ctx

@auto_render
def new(request):
    if request.method =='GET':
        form = f.NewForm()
    else:
        form = f.NewForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return auto_redirect('detail',pk=obj.pk)

    ctx = {}
    ctx['form'] = form
    return ctx

@auto_render
def edit(request,pk):
    obj = m.M.objects.get(pk=pk)
    if request.method =='GET':
        form = f.EditForm(instance=obj)
    else:
        form = f.EditForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return auto_redirect('detail',pk=obj.pk)

    ctx = {}
    ctx['form'] = form
    return ctx

@auto_render
def detail(request,pk):
    obj = m.M.objects.get(pk=pk)
    form = f.DetailForm(instance=obj,readonly=True)
    ctx = {}
    ctx['obj'] = obj
    ctx['form'] = form
    return ctx

def delete(request,pk):
    obj = m.M.objects.get(pk=pk)
    obj.delete()
    return auto_redirect('index')
