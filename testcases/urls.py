from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='testcases'),
    path('testcases_mcqs/<test_set>',views.mcqs,name='testcases_mcqs'),
    path('testcases_diagnosis',views.diagnosis,name='testcases_diagnosis'),
    path('testcases_mcq_submit',views.submit_mcq,name='submit_mcq')
]