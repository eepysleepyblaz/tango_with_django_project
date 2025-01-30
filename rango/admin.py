from django.contrib import admin

#Pg 76 TwD
from rango.models import Category, Page

#Pg88 TwD
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
