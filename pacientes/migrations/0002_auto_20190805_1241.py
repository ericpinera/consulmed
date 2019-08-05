# Generated by Django 2.0.7 on 2019-08-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='tipo_identificacion',
            field=models.CharField(choices=[('cedula', 'Cédula'), ('pasaporte', 'Pasaporte')], default='cedula', max_length=20, verbose_name='Tipo identificacion'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='primerApellido',
            field=models.CharField(max_length=250, verbose_name='Primer apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='primerNombre',
            field=models.CharField(max_length=250, verbose_name='Primer nombre'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='segundoApellido',
            field=models.CharField(max_length=250, verbose_name='Segundo apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='segundoNombre',
            field=models.CharField(max_length=250, verbose_name='Segundo nombre'),
        ),
    ]