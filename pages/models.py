from django.db import models
from lessons.models import Lesson
from django.contrib.auth.models import User

# Create your models here.

class Progress(models.Model):
    #user_name = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.IntegerField(unique=True,blank=True,null=True)
    prog_LM = models.IntegerField(default=0)
    #prog_LM_th = models.IntegerField(default=0)
    #prog_LM_pc = models.IntegerField(default=0)
    kidney_LM_th = models.BooleanField(default=False)
    kidney_LM_pc_1 = models.BooleanField(default=False)
    kidney_LM_pc_2 = models.BooleanField(default=False)
    kidney_LM_pc_3 = models.BooleanField(default=False)
    headneck_LM_th = models.BooleanField(default=False)
    headneck_LM_pc_1 = models.BooleanField(default=False)
    headneck_LM_pc_2 = models.BooleanField(default=False)
    headneck_LM_pc_3 = models.BooleanField(default=False)
    lung_LM_th = models.BooleanField(default=False)
    lung_LM_pc_1 = models.BooleanField(default=False)
    lung_LM_pc_2 = models.BooleanField(default=False)
    lung_LM_pc_3 = models.BooleanField(default=False)

    prog_TM = models.IntegerField(default=0)
    
    #prog_TM_mcq = models.IntegerField(default=0)
    #prog_TM_pc = models.IntegerField(default=0)
    #theory_prog = models.IntegerField(blank=True,null=True)
    #def __str__(self):
        #return self.user_name