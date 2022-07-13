from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
#from pages.models import Progress

# Create your models here.

class Lesson(models.Model):
    disease_id = models.BigAutoField(primary_key=True)
    disease_type = models.CharField(max_length=50)
    disease_line = models.TextField(blank=True)
    image_organ1 = models.ImageField(upload_to='photos/', blank=True)  #lesson_thumbnail
    image_organ2 = models.ImageField(upload_to='photos/', blank=True)  #lesson theory
    image_prevention = models.ImageField(upload_to='photos/', blank=True)  #lesson prevention
    theory = models.TextField(blank=True)
    do_and_dont = models.TextField(blank=True)
    theory_progress = models.IntegerField(blank=True,null=True) 
    #user_id = models.ForeignKey(User)
    def __str__(self):
        return self.disease_type

class Lesson_pc(models.Model):
    disease_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    model_id = models.CharField(max_length=50)
    filename = models.TextField(blank=True)
    testcase = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    prior_malignancies = models.CharField(max_length=50)
    primary_tumor_site = models.TextField(blank=True)
    alcohol_history = models.CharField(max_length=50)
    smoking_history = models.TextField(blank=True)
    cancer_type = models.TextField(blank=True)
    basic_cancer_type = models.TextField(blank=True)
    def __str__(self):
        return self.filename

