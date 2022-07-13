from django.contrib import admin

# Register your models here.

from .models import Lesson, Lesson_pc

admin.site.register(Lesson)
admin.site.register(Lesson_pc)