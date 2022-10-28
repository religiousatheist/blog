from pathlib import Path
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('contact',views.contact,name='contact'),
    path('part1',views.part1,name='part1' ),
    path('god',views.god,name='god'),
    path('science',views.science,name='science')
]