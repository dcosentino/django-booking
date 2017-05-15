# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Manager, ManagerAdmin)

class ShowAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Show, ShowAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Location, LocationAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['ts', 'show']
    date_hierarchy = 'ts'
admin.site.register(Event, EventAdmin)
