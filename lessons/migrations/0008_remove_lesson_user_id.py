# Generated by Django 3.2.5 on 2022-02-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_lesson_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='user_id',
        ),
    ]
