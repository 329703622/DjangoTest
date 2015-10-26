# coding=utf-8
from django.db import models
from django.contrib import admin

class Doc(models.Model):
    title     = models.CharField(u'标题',max_length=128)
    author    = models.CharField(u'作者',max_length=128)
    date      = models.CharField(u'年份',max_length=10)
    source    = models.CharField(u'出处',max_length=128)

class DocPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date','source')

admin.site.register(Doc,DocPostAdmin)