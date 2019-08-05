from django.db import models
from pacientes.models import Paciente

# Create your models here.
class Cita(models.Model):
    horario_opciones = (
        ('turno_1', '8:00 - 9:00'),
        ('turno_2', '9:00 - 10:00'),
        ('turno_3', '10:00 - 11:00'),
        ('turno_4', '11:00 - 12:00'),
        ('turno_5', '12:00 - 13:00'),
        ('turno_6', '13:00 - 14:00'),
        ('turno_7', '14:00 - 15:00'),
        ('turno_8', '15:00 - 16:00'),
        ('turno_9', ' 16:00 - 17:00'),
        ('turno_10', '17:00 - 18:00'),
        ('turno_11', '18:00 - 19:00'),
        ('turno_12', '19:00 - 20:00'),
        ('turno_13', '20:00 - 21:00'),
        ('turno_14', ' 21:00 - 22:00')
    )
    estado_opciones = (
        ('pendiente', 'Pendiente'),
        ('finalizada', 'Finalizada'),
        ('anulada', 'Anulada')
    )
    fecha =     models.DateField('Fecha', auto_now_add=False)
    horario =   models.CharField('Horario',
                                    max_length=20,
                                    choices =  horario_opciones,
                                    default="Seleccionar")
    estado =    models.CharField('Estado',
                                    max_length=20,
                                    choices =  estado_opciones,
                                    default='pendiente')
    paciente =  models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)                                

