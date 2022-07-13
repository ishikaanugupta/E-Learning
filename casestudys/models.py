from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from pathlib import Path
from django.conf import settings

# Create your models here.

class myuploadfile(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    
    def upload_file(instance, filename):
        try:
            path = "dicom/{id}/{file}".format(id="guest", file=filename)
            return path
        except User.DoesNotExist:
            pass

    myfiles = models.FileField(upload_to=upload_file)


