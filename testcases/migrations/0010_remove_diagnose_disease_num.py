# Generated by Django 3.2.5 on 2022-03-19 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0009_diagnose_disease_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnose',
            name='disease_num',
        ),
    ]
