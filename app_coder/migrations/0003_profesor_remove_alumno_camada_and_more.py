# Generated by Django 4.0.4 on 2022-07-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_alumno_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='camada',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='nombre',
        ),
    ]
