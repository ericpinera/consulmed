# Generated by Django 2.0.7 on 2019-08-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerNombre', models.CharField(max_length=250)),
                ('segundoNombre', models.CharField(max_length=250)),
                ('primerApellido', models.CharField(max_length=250)),
                ('segundoApellido', models.CharField(max_length=250)),
            ],
        ),
    ]
