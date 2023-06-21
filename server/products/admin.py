from django.contrib import admin
from .models import Products
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'prise', 'id']
    list_display_links = ['title', 'prise', 'id']
    list_filter = ['title', 'prise']
    search_fields = ['title', 'prise', 'descreption']


admin.site.register(Products, ProductAdmin)
