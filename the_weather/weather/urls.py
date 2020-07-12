from django.contrib import admin
from weather.views import *
from django.urls import path
urlpatterns = [
    path('',index,name='index_page'),
    path('delete/<city_name>/',delete_city,name='delete_city')
]