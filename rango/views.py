from django.shortcuts import render


#Pg34 TwD
from django.http import HttpResponse

def index(request):
    #Pg48 TwD
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

#Pg40 TwD
def about(request):
    #Pg63 TwD
    context_dict = {'boldmessage': 'This tutorial has been put together by Sandy'}
    return render(request, 'rango/about.html', context=context_dict)
