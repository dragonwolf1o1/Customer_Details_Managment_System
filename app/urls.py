from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginuser,name='login'),
    path('forget',views.forget,name='forget'),
    path('customer/<str:val>',views.customer,name='customer'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('add_customer',views.addc,name='addc'),
    path('about',views.about,name='about'),
    path('logout',views.logoutuser,name='logout'),
    path('search',views.search,name='search'),
]
