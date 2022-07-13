from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mcq(models.Model):
    ques_id = models.BigAutoField(primary_key=True)
    test_set = models.TextField(blank=True)
    test_set_id = models.IntegerField(blank=True,null=True)
    ques_txt = models.TextField(blank=True)
    ques_num = models.IntegerField(blank=True,null=True)
    opt_A = models.TextField(blank=True)
    opt_B = models.TextField(blank=True)
    opt_C = models.TextField(blank=True)
    opt_D = models.TextField(blank=True)
    corr_opt = models.CharField(max_length=50)
    def __str__(self):
        return self.test_set + " Ques:" + str(self.ques_id)

class Mcq_score(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    test_set_new = models.TextField(blank=True)
    score = models.IntegerField(blank=True,null=True)

class Diagnose(models.Model):
    directory_name = models.TextField(blank=True)
    disease = models.TextField(blank=True)
    def __str__(self):
      return self.directory_name  + " " + self.disease

