# Generated by Django 3.2.5 on 2022-03-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_alter_lesson_pc_disease_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_pc',
            name='testcase',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]