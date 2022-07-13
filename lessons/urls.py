from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('',views.index, name='lessons'),
    path('lessons_theory/<int:disease_id>',views.theory,name='lessons_theory'),
    path('lessons_patientcases/<int:disease_id>',views.patientcases,name='lessons_patientcases'),
    #path('lessons_patientcases/<int:disease_id>',views.patientcases_model,name='lessons_patientcases_model'),
    path('lessons_patientcases/<int:disease_id>/lessons_model/<int:model_id>',views.model,name='lessons_model'),
]