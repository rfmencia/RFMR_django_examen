from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

def examen_ets(value):
    if 'E.T.S' in value.upper() or 'ETS' in value.upper():
        raise ValidationError("No se deben registrar los laboratorios E.T.S en los exámenes realizados por confidencialidad")

def fecha_paciente(value):
    print()
    if value > (timezone.now() + timedelta(days=15)).date():
        raise ValidationError("Solo se puede programar la atencion hasta dentro de 15 dias")
