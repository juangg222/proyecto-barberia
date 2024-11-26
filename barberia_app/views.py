from django.shortcuts import render, redirect
from .forms import AgendaForm  # Importar el formulario
from .models import Formulario  # Importar el modelo para guardar los datos

def home(request):
    return render(request, 'home.html')

def servicios(request):
    return render(request, 'servicios.html')

def agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)  # Recibir los datos del formulario
        if form.is_valid():  # Verificar que los datos sean válidos
            form.save()  # Guardar el formulario en la base de datos
            return redirect('confirmacion')  # Redirigir a la página de confirmación
    else:
        form = AgendaForm()  # Crear un formulario vacío si la solicitud es GET
    
    return render(request, 'agenda.html', {'form': form})  # Renderizar el formulario

def confirmacion(request):
    return render(request, 'confirmacion.html')  # Mostrar la página de confirmación
