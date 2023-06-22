from django.db import models
from django.core.validators import EmailValidator
from .validators import examen_ets,fecha_paciente

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(validators=[EmailValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Atencion(models.Model):
    MEDICOS_CHOICES = [
        ('Dr Perez', 'Dr. Juan Perez'),
        ('Dra Gomez', 'Dra. Ana Gomez'),
        ('Dr Rodriguez', 'Dr. Carlos Rodriguez'),
        ('Dra Sanchez', 'Dra. Laura Sanchez'),
        ('Dr Lopez', 'Dr. Martin Lopez'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.CharField(max_length=100, choices=MEDICOS_CHOICES)
    motivo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva de {self.paciente} el {self.fecha}"


class Laboratorio(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(validators=[fecha_paciente])
    examenes_realizados = models.TextField(validators=[examen_ets],help_text="Ingrese los laboratorios realizados separados por comas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Laboratorio de {self.paciente} el {self.fecha}"


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(validators=[fecha_paciente])
    diagnostico = models.TextField()
    recomendaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consulta de {self.paciente} el {self.fecha}"
