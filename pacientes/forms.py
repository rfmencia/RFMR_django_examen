from django import forms
from .models import Paciente, Atencion, Consulta, Laboratorio

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'telefono', 'email', 'activo']

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['paciente', 'fecha', 'hora', 'medico', 'motivo']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'fecha', 'diagnostico', 'recomendaciones']
        
class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['paciente', 'fecha', 'examenes_realizados']