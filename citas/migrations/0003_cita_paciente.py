# Generated by Django 2.0.7 on 2019-08-05 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20190805_1615'),
        ('citas', '0002_auto_20190805_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
        ),
    ]
