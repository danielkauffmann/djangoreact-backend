from django.contrib import admin
from .models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'list', 'done']
