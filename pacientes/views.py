from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, AtencionForm, ConsultaForm, LaboratorioForm
from .models import Paciente, Atencion, Consulta, Laboratorio
from .serializers import PacienteSerializer,AtencionSerializer
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

# Ver registros
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def lista_atenciones(request):
    atenciones = Atencion.objects.all()
    return render(request, 'lista_atenciones.html', {'atenciones': atenciones})

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios})

# Crear registros
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'agregar_paciente.html', {'form': form})

def agregar_atencion(request):
    if request.method == 'POST':
        form = AtencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atenciones')
    else:
        form = AtencionForm()
    return render(request, 'agregar_atencion.html', {'form': form})

def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'agregar_consulta.html', {'form': form})

def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'agregar_laboratorio.html', {'form': form})

# Buscar y eliminar registros
def buscar_paciente(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        pacientes = Paciente.objects.filter(nombre__icontains=query)
        return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
    return redirect('lista_pacientes')

def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'eliminar_paciente.html', {'paciente': paciente})

# Serializadores

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AtencionViewSet(viewsets.ModelViewSet):
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer

class PacienteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
# Custom API
@api_view(["GET"])
def paciente_count(request):
    try:
        cantidad = Paciente.objects.count()
        return JsonResponse(
                {
                    "cantidad": cantidad
                },
                safe=False,
                status=200
            )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)