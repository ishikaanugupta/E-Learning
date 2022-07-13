# Generated by Django 3.2.5 on 2022-02-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('disease_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('disease_type', models.CharField(max_length=50)),
                ('image_organ', models.ImageField(upload_to='photos/')),
                ('image_prevention', models.ImageField(upload_to='photos/')),
                ('theory', models.TextField(blank=True)),
                ('do_and_dont', models.TextField(blank=True)),
                ('theory_progress', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
