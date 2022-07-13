from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages, auth
from .models import Progress
from testcases.models import Mcq_score
from django.db.models import Count


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

#def lessons(request):
    #return render(request, 'pages/lessons.html')

def testcase(request):
    return render(request, 'pages/testcase.html')

def casestudy(request):
    return render(request, 'pages/casestudy.html')

def dashboard(request):
    if Progress.objects.filter(user_id = request.user.id).exists():
        progress = Progress.objects.get(user_id = request.user.id)
        lm_th_perc = 0
        lm_pc_perc = 0
        if progress.kidney_LM_th:
            lm_th_perc += 1
        if progress.headneck_LM_th:
            lm_th_perc += 1
        if progress.lung_LM_th:
            lm_th_perc += 1
        lm_th_perc = round((lm_th_perc/3)*100)
        if progress.kidney_LM_pc_1:
            lm_pc_perc += 1
        if progress.kidney_LM_pc_2:
            lm_pc_perc += 1
        if progress.kidney_LM_pc_3:
            lm_pc_perc += 1
        if progress.headneck_LM_pc_1:
            lm_pc_perc += 1
        if progress.headneck_LM_pc_2:
            lm_pc_perc += 1
        if progress.headneck_LM_pc_3:
            lm_pc_perc += 1
        if progress.lung_LM_pc_1:
            lm_pc_perc += 1
        if progress.lung_LM_pc_2:
            lm_pc_perc += 1
        if progress.lung_LM_pc_3:
            lm_pc_perc += 1
        lm_pc_perc = round((lm_pc_perc/9)*100)
        lm_perc = round((progress.prog_LM/12) * 100)

        
        test = Mcq_score.objects.filter(user_id = request.user.id).values()

       
        print(test)
        print(len(test))

        tm_perc = round((len(test)/6)*100)



        context = {
        "progress":progress, 
        "lm_th_perc": lm_th_perc,
        "lm_pc_perc": lm_pc_perc,
        "lm_perc": lm_perc,
        "tm_perc":tm_perc
        }

    return render(request, 'pages/dashboard.html', context)
