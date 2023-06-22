from django.contrib import admin
from .models import Paciente
from .models import Atencion
from .models import Laboratorio
from .models import Consulta

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'email', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'apellido', 'telefono', 'email']
    date_hierarchy = 'fecha_nacimiento'
   
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Atencion)
admin.site.register(Laboratorio)
admin.site.register(Consulta)