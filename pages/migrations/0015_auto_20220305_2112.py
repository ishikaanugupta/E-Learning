# Generated by Django 3.2.5 on 2022-03-05 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='prog_LM_pc',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='prog_LM_th',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='prog_TM_mcq',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='prog_TM_pc',
        ),
    ]
