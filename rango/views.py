from django.shortcuts import render

#Pg34 TwD
from django.http import HttpResponse

def index(request):
    #Pg48 TwD
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

#Pg40 TwD
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>.")
