# Generated by Django 3.2.5 on 2022-02-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='theory_progress',
        ),
    ]
