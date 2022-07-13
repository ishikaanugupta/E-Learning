from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from .models import Mcq, Mcq_score, Diagnose
from django.db.models import Count
import random
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    mcqs = Mcq.objects.all()
    grp_mcqs = Mcq.objects.values('test_set_id','test_set').annotate(dcount=Count('test_set_id')).order_by()
        

    if Mcq_score.objects.filter(user_id = request.user.id).exists():
        user_mcq_score = Mcq_score.objects.filter(user_id = request.user.id).values()

    else:
        user_mcq_score = [0,0,0,0,0,0]
        
        pass

    #messages.info(request, "You have to attempt the quiz")

    context = {
    'mcqs':mcqs,
    'grp_mcqs':grp_mcqs,
    'user_mcq_score':user_mcq_score
    }
    return render(request,'testcases/testcases.html',context)

def mcqs(request, test_set):
    if request.user.is_authenticated:
        mcqs = Mcq.objects.filter(test_set = test_set)

        context = {
             'mcqs':mcqs,
        }


        return render(request,'testcases/testcases_mcqs.html', context)

    else:
        messages.warning(request, "You need to register to access this module")
        return redirect('/testcases/')

def submit_mcq(request):
    print(request.POST)

    data = dict(request.POST)

    print(data)

    user_id = data["user_id"][0]
    print(user_id[0])

    data.pop("csrfmiddlewaretoken")
    data.pop("user_id")

    print(data)

    corr = 0

    for key,value in data.items():
        ques = Mcq.objects.filter(ques_id = key).values()
        ques_dict = dict(ques[0])
        corr_ans = ques_dict["corr_opt"]
        test_set = ques_dict["test_set"]
        user_ans = value[0]

        if user_ans == corr_ans:
            corr += 1

    if Mcq_score.objects.filter(user_id = user_id, test_set_new=test_set).exists():
        mcq_update = Mcq_score.objects.get(user_id = user_id, test_set_new=test_set)
        #print(mcq_update)
        mcq_update.score = corr
        mcq_update.save()
    else:
        mcq_score = Mcq_score.objects.create(user_id=user_id, test_set_new = test_set, score = corr)
        mcq_score.save()
            
    context = {
        'corr':corr
    }


    return render(request,'testcases/testcases_mcq_submit.html', context)

def random_func():
    diag_list = []
    diag = Diagnose.objects.values('directory_name')
    
    for i in diag:
        diag_list.append(i['directory_name'])
    print(diag_list)

    directory = random.choice(diag_list)

    return directory


def diagnosis(request):
    if request.user.is_authenticated:
        if request.method!= "POST":

            directory = random_func()
            print(directory)

            context={
                'directory':directory
            }
            return render(request,'testcases/testcases_diagnosis.html', context)

        else:
            print(request.POST)

            data = dict(request.POST)
            print(data)
            print(data['disease_name'][0])
            directory_n = data['disease_name'][0]

            #Checking the answer from database
            user_ans = data['disease'][0]
            print(directory_n)
            corr_ans_query = Diagnose.objects.filter(directory_name = directory_n).values()
            corr_ans_dict = dict(corr_ans_query[0])
            corr_ans = corr_ans_dict['disease']
            
            print("User answer", user_ans)
            print("Correct answer",corr_ans)
            
            if user_ans == corr_ans:
                messages.info(request, "The answer is CORRECT")
                messages.success(request, "Moving on to next patient model")
                directory_n = random_func()
                
               
            else:
                messages.info(request, "The answer is WRONG")
                messages.warning(request, "Try again")
                

            context={
                'directory':directory_n
            }


           
            return render(request,'testcases/testcases_diagnosis.html', context)

    
    else:
        messages.warning(request, "You need to register to access this module")
        return redirect('/testcases/')
    

