from django.shortcuts import render

#Pg92 TwD
from rango.models import Category

#Pg101 TwD
from rango.models import Page

#Pg127 TwD
from rango.forms import PageForm

#Pg128 TwD
from django.urls import reverse

#Pg117 TwD
from rango.forms import CategoryForm

from django.shortcuts import redirect

#Pg34 TwD
from django.http import HttpResponse

#Pg172 TwD
from django.contrib.auth import authenticate, login, logout

#Pg170 TwD
from django.contrib.auth.decorators import login_required

#Pg157 TwD
from rango.forms import UserForm, UserProfileForm

#Pg185 TwD
from datetime import datetime


def index(request):
    #Pg92 TwD
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    
    #Pg186 TwD
    context_dict['visits'] = int(request.COOKIES.get('visits', '1'))

    #Pg185-186 TwD
    response = render(request, 'rango/index.html', context=context_dict)

    visitor_cookie_handler(request, response)
    return response

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


#Pg116 TwD
@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})

#Pg127 TwD
@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

#Pg157 TwD
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'rango/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})

#Pg164 TwD
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    
    else:
        return render(request, 'rango/login.html')
    
#Pg170
@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

#Pg172
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

#Pg184 TwD
def visitor_cookie_handler(request, responce):
    visits = int(request.COOKIE.get('visits', '1'))

    last_visit_cookie = request.COOKIE.get('last_visit', str(datetime.now))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        responce.set_cookie('last_visit', str(datetime.now()))
    else:
        responce.set_cookie('last_visit', last_visit_cookie)
    
    responce.set_cookie('visits', visits)