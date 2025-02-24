#Pg 37 TwD
from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),

    #Pg104 TwD
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),

    #Pg120 TwD
    path('add_category/', views.add_category, name='add_category'),

    #Pg126 TwD
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),

    #Pg161 TwD
    path('register/', views.register, name='register'),

    #Pg167 TwD
    path('login/', views.user_login, name='login'),

    #Pg170 TwD
    path('restricted/', views.restricted, name='restricted'),

    #Pg172 TwD
    path('logout/', views.user_logout, name='logout'),
]