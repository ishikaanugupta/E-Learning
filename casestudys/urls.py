from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='casestudys'),
    path('casestudys_model',views.send_files,name='casestudys_model'),
]