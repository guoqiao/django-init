# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class BaseGenericModel(models.Model):
    content_type   = models.ForeignKey(ContentType)
    object_id      = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        abstract = True

class Comment(BaseGenericModel):
    text = models.TextField()
    removed = models.BooleanField(default=False)

    user = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)

SCORE_VALUE_CHOICES = (
    ('-5',-5),
    ('-4',-4),
    ('-3',-3),
    ('-2',-2),
    ('-1',-1),
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
)

class Score(BaseGenericModel):
    value = models.IntegerField(choices=SCORE_VALUE_CHOICES)

    user = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)

class TaggedSnippet(TaggedItemBase):
    content_object = models.ForeignKey('Snippet')

class Snippet(models.Model):
    title = models.CharField(max_length=128)
    code = models.TextField()
    desc = models.TextField()
    tags = TaggableManager(blank=True, through=TaggedSnippet)
    user = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

admin.site.register(Snippet)
admin.site.register(Comment)
admin.site.register(Score)
