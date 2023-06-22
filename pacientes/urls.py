from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"pacientes", views.PacienteViewSet)
router.register(r"atenciones", views.AtencionViewSet)

urlpatterns = [
    # Ver registros
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('atenciones/', views.lista_atenciones, name='lista_atenciones'),
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('laboratorios/', views.lista_laboratorios, name='lista_laboratorios'),

    # Agregar registros
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('agregar_atencion/', views.agregar_atencion, name='agregar_atencion'),
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('agregar_laboratorio/', views.agregar_laboratorio, name='agregar_laboratorio'),

    # Buscar pacientes
    path('buscar_paciente/', views.buscar_paciente, name='buscar_paciente'),

    # Eliminar pacientes
    path('eliminar_paciente/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    
    # G.APIview 
    path("pacientes_crear_listar", views.PacienteCreateView.as_view(), name="pacientes_crear"),
    
    # M. Setview
    path("", include(router.urls)),
    
    # CustomAPI
    path("pacientes/cantidad", views.paciente_count, name="paciente_count"),
]
