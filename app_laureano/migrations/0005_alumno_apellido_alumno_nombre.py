# Generated by Django 4.0.4 on 2022-07-03 19:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_laureano', '0004_profesor_apellido_profesor_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
