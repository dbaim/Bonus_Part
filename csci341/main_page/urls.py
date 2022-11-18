from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main_page'),
    path('edit', views.edit, name='edit'),
    path('country_insert', views.insert1, name='insert1'),
    path('dt_insert', views.insert2, name='insert2'),
    path('dis_insert', views.insert3, name='insert3'),
    path('discovery_insert', views.insert4, name='insert4'),
    path('users_insert', views.insert5, name='insert5'),
    path('doctor_insert', views.insert6, name='insert6'),
    path('publicservant_insert', views.insert7, name='insert7'),
    path('record_insert', views.insert8, name='insert8'),
    path('specialize_insert', views.insert9, name='insert9'),
    path('delete1/<str:cname>', views.delete1, name='delete1'),
    path('delete2/<int:id>', views.delete2, name='delete2'),
    path('delete3/<str:disease_code>', views.delete3, name='delete3'),
    path('delete4/<str:disease_code>', views.delete4, name='delete4'),
    path('delete5/<str:email>', views.delete5, name='delete5'),
    path('delete6/<str:email>', views.delete6, name='delete6'),
    path('delete7/<str:email>', views.delete7, name='delete7'),
    path('delete8/<str:email>', views.delete8, name='delete8'),
    path('delete9/<str:email>', views.delete9, name='delete9')
]