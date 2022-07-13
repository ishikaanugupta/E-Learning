from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    #path('lessons',views.lessons,name='lessons'),
    #path('testcase',views.testcase,name='testcase'),
    #path('casestudy',views.casestudy,name='casestudy'),
    path('dashboard',views.dashboard,name='dashboard')
]