# Generated by Django 3.2.5 on 2022-02-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_remove_lesson_disease_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='disease_line',
            field=models.TextField(blank=True),
        ),
    ]
