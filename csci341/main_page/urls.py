from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main_page'),
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
    path('delete9/<str:email>', views.delete9, name='delete9'),
    path('edit1/<str:cname>', views.edit1, name='edit1'),
    path('update1/<str:cname>', views.update1, name="update1"),
    path('edit2/<int:id>', views.edit2, name='edit2'),
    path('update2/<int:id>', views.update2, name="update2"),
    path('edit3/<str:disease_code>', views.edit3, name='edit3'),
    path('update3/<str:disease_code>', views.update3, name="update3"),
    path('edit4/<str:disease_code>', views.edit4, name='edit4'),
    path('update4/<str:disease_code>', views.update4, name="update4"),
    path('edit5/<str:email>', views.edit5, name='edit5'),
    path('update5/<str:email>', views.update5, name="update5"),
    path('edit6/<str:email>', views.edit6, name='edit6'),
    path('update6/<str:email>', views.update6, name="update6"),
    path('edit7/<str:email>', views.edit7, name='edit7'),
    path('update7/<str:email>', views.update7, name="update7"),
    path('edit8/<str:email>', views.edit8, name='edit8'),
    path('update8/<str:email>', views.update8, name="update8"),
    path('edit9/<str:email>', views.edit9, name='edit9'),
    path('update9/<str:email>', views.update9, name="update9")
]