from django.db import models

# Create your models here.
class Paciente(models.Model):
    tipo_identificacion_opciones = (
        ('cedula', 'Cédula'),
        ('pasaporte', 'Pasaporte')
    )

    sexo_opciones = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro')
    )

    primerNombre =          models.CharField('Primer nombre',  max_length=250)
    segundoNombre =         models.CharField('Segundo nombre', max_length=250)
    primerApellido =        models.CharField('Primer apellido', max_length=250)
    segundoApellido =       models.CharField('Segundo apellido', max_length=250)
    tipo_identificacion =   models.CharField('Tipo identificacion',
                                                max_length=20,
                                                choices =  tipo_identificacion_opciones,
                                                default='cedula')
    identificacion =        models.CharField('Identificación', max_length=50, null=True)
    sexo =                  models.CharField('Sexo',
                                                max_length=20,
                                                choices =  sexo_opciones,
                                                default='femenino')
    direccion =             models.TextField('Dirección', null=True)
    telefono =              models.CharField('Teléfono', max_length=100, null=True)
    correo =                models.EmailField('Email', null=True)                                          


