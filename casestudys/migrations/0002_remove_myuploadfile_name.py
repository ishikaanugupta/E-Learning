# Generated by Django 3.2.5 on 2022-03-03 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfile',
            name='name',
        ),
    ]