from django.contrib import admin

# Register your models here.

from .models import Mcq, Mcq_score,Diagnose


admin.site.register(Mcq)
admin.site.register(Mcq_score)
admin.site.register(Diagnose)
