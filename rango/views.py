from django.shortcuts import render

#Pg92 TwD
from rango.models import Category

#Pg101 TwD
from rango.models import Page

#Pg34 TwD
from django.http import HttpResponse

def index(request):
    #Pg92 TwD
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

#Pg40 TwD
def about(request):
    #Pg63 TwD
    context_dict = {'boldmessage': 'This tutorial has been put together by Sandy'}
    return render(request, 'rango/about.html', context=context_dict)


#Pg102 TwD
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)