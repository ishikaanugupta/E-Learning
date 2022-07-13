from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages, auth
from .models import Lesson, Lesson_pc
from pages.models import Progress

# Create your views here.

def index(request):
    lessons = Lesson.objects.all()

    context = {
        'lessons':lessons
        
    }
    return render(request,'lessons/lessons.html', context)

def theory(request, disease_id):
    if request.user.is_authenticated:
        lessons = get_object_or_404(Lesson, pk=disease_id)
        

        context = {
        'lessons':lessons
        
        }
        return render(request,'lessons/lessons_theory.html', context)

    else:
        messages.warning(request, "You need to register to access this module")
        return redirect('/lessons/')

def patientcases(request, disease_id):
    if request.user.is_authenticated:
        #lessons_pcs = get_object_or_404(Lesson_pc, disease_id=disease_id)
        lessons_pcs = Lesson_pc.objects.filter(disease_id = disease_id)
        if Progress.objects.filter(user_id=request.user.id).exists():
            progress = Progress.objects.get(user_id=request.user.id)
            if disease_id == 1:
                if not progress.kidney_LM_th:
                    progress.prog_LM += 1              
                progress.kidney_LM_th = True
            elif disease_id == 2:
                if not progress.headneck_LM_th:
                    progress.prog_LM += 1
                progress.headneck_LM_th = True
            elif disease_id == 3:
                if not progress.lung_LM_th:
                    progress.prog_LM += 1
                progress.lung_LM_th = True
            progress.save()
            
        else:
            progress = Progress.objects.create(user_id=request.user.id)
            if disease_id == 1:
                if not progress.kidney_LM_th:
                    progress.prog_LM += 1              
                progress.kidney_LM_th = True
                progress.save()
        context = {
        'lessons_pcs':lessons_pcs,
        'progress':progress
        }
        return render(request,'lessons/lessons_patientcases.html', context)

    else:
        messages.warning(request, "You need to register to access this module")
        return redirect('/lessons/')
    

def model(request, disease_id, model_id):
    lessons_model = get_object_or_404(Lesson_pc, disease_id=disease_id, model_id=model_id)

    if Progress.objects.filter(user_id=request.user.id).exists():
            progress = Progress.objects.get(user_id=request.user.id)
            if disease_id == 1:
                if not progress.kidney_LM_pc_1 or not progress.kidney_LM_pc_2 or not progress.kidney_LM_pc_3:
                    progress.prog_LM += 1  
                if model_id == 1:            
                    progress.kidney_LM_pc_1 = True
                elif model_id == 2:
                    progress.kidney_LM_pc_2 = True
                elif model_id == 3:
                    progress.kidney_LM_pc_3 = True
                progress.save()
            elif disease_id == 2:
                if not progress.headneck_LM_pc_1 or not progress.headneck_LM_pc_2 or not progress.headneck_LM_pc_3:
                    progress.prog_LM += 1
                if model_id == 1:            
                    progress.headneck_LM_pc_1 = True
                elif model_id == 2:
                    progress.headneck_LM_pc_2 = True
                elif model_id == 3:
                    progress.headneck_LM_pc_3 = True
                progress.save()
            elif disease_id == 3:
                if not progress.lung_LM_pc_1 or not progress.lung_LM_pc_2 or not progress.lung_LM_pc_3:
                    progress.prog_LM += 1
                if model_id == 1:            
                    progress.lung_LM_pc_1 = True
                elif model_id == 2:
                    progress.lung_LM_pc_2 = True
                elif model_id == 3:
                    progress.lung_LM_pc_3 = True
                progress.save()

    context = {
        'lessons_model':lessons_model
    }
    return render(request, 'lessons/lessons_model.html', context)

def patientcases_model(request, disease_id):
    if Progress.objects.filter(user_id=request.user.id).exists():
        progress = Progress.objects.get(user_id=request.user.id)
        if disease_id == 1:
            if not progress.kidney_LM_th:
                progress.prog_LM += 1              
            progress.kidney_LM_th = True
        elif disease_id == 2:
            if not progress.headneck_LM_th:
                progress.prog_LM += 1
            progress.headneck_LM_th = True
        elif disease_id == 3:
            if not progress.lung_LM_th:
                progress.prog_LM += 1
            progress.lung_LM_th = True
        progress.save()
            
    else:
        progress = Progress.objects.create(user_id=request.user.id)
        if disease_id == 1:
            if not progress.kidney_LM_th:
                progress.prog_LM += 1              
            progress.kidney_LM_th = True
            progress.save()            

    context = {
    'progress':progress
    }
    return render(request,'lessons/lessons_patientcases.html', context)