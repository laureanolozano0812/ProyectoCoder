# Generated by Django 4.0.4 on 2022-07-03 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_laureano', '0003_profesor_remove_alumno_camada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
