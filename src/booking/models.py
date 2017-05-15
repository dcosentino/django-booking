# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from utils.safestrings import *

from ckeditor.fields import RichTextField

from django import forms
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe

class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta(object):
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name)

class Manager(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta(object):
        verbose_name_plural = 'manager'
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.manager)

class Show(models.Model):
    def upload_img(instance, filename):
        return u"spettacoli/%s" % (sanitize_path(filename))

    manager = models.ForeignKey(Manager)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256)
    abstract = models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=sanitized_upload_to, help_text='Dimensione 300x225px')
    alt_image = models.CharField(max_length=256, null=True, blank=True)
    
    class Meta(object):
        verbose_name_plural = 'shows'
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return reverse('spettacolo', args=[slugify(self.title)])


class Location(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta(object):
        verbose_name_plural = 'locations'
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % (self.name)

    def get_absolute_url(self):
        return reverse('location', args=[slugify(self.name)])

class Event(models.Model):
    def upload_img(instance, filename):
        return u"eventi/%s" % (sanitize_path(filename))

    show = models.ForeignKey(Show)
    location = models.ForeignKey(Location)
    published = models.BooleanField(default=False)
    ts = models.DateTimeField()

    class Meta(object):
        verbose_name_plural = 'events'
        ordering = ['-ts']

    def __unicode__(self):
        return u'%s' % (self.show.title, self.ts.strftime('%d/%m/%Y'))

    def get_absolute_url(self):
        return reverse('eventi', args=[slugify(self.show.title), self.ts.strftime('%d/%m/%Y')])


