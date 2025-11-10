from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitacion

def inicio(request):
    return render(request, 'inicio.html')

# ✅ VER HABITACIONES
def ver_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacion/ver_habitacion.html', {'habitaciones': habitaciones})

# ✅ AGREGAR HABITACION
def agregar_habitacion(request):
    if request.method == 'POST':
        Habitacion.objects.create(
            numero=request.POST['numero'],
            tipo=request.POST['tipo'],
            precio=request.POST['precio'],
            capacidad=request.POST['capacidad'],
            ocupada=True if request.POST.get('ocupada') == 'on' else False,
            ubicacion=request.POST['ubicacion']
        )
        return redirect('ver_habitaciones')

    return render(request, 'habitacion/agregar_habitacion.html')

# ✅ FORMULARIO DE ACTUALIZACION
def actualizar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    if request.method == 'POST':
        return realizar_actualizacion_habitacion(request, id)

    return render(request, 'habitacion/actualizar_habitacion.html', {'habitacion': habitacion})

# ✅ GUARDAR ACTUALIZACION
def realizar_actualizacion_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    habitacion.numero = request.POST['numero']
    habitacion.tipo = request.POST['tipo']
    habitacion.precio = request.POST['precio']
    habitacion.capacidad = request.POST['capacidad']
    habitacion.ocupada = True if request.POST.get('ocupada') == 'on' else False
    habitacion.ubicacion = request.POST['ubicacion']

    habitacion.save()
    return redirect('ver_habitaciones')

# ✅ BORRAR HABITACION
def borrar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    if request.method == 'POST':
        habitacion.delete()
        return redirect('ver_habitaciones')

    return render(request, 'habitacion/borrar_habitacion.html', {'habitacion': habitacion})
