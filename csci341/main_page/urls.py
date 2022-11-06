from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main_page'),
    path('edit', views.edit, name='edit'),
    path('insert', views.insert, name='insert')
]