# Generated by Django 2.0.7 on 2019-08-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_auto_20190805_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='correo',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
    ]
