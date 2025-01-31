from django.contrib import admin

#Pg 76 TwD
from rango.models import Category, Page

#Pg88 TwD
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

#Pg100 TwD
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
