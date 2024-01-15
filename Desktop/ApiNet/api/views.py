from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .forms import *
from .models import *


def index(request):
    return render(request, "index.html",{})


def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_employee')
    else:
        form = EmployeeForm()

    # Obtiene instancias de las tablas relacionadas para pasarlas al contexto
    subareas = Subarea.objects.all()
    documenttypes = DocumentType.objects.all()
    areas = Area.objects.all()
    countries = Country.objects.all()

    return render(request, 'api/newemployee.html', {'form': form, 'subareas': subareas, 'documenttypes': documenttypes, 'areas': areas, 'countries': countries})



def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})



def delete_employee(request, employee_id):
    # Obtiene el objeto que deseas eliminar
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        # Elimina el empleado y sus relaciones
        employee.delete()
        return JsonResponse({'success': True, 'redirect_url': reverse('ver_employee')})

    # Si la solicitud no es POST, devuelve un error
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def ver_employee(request):
    # Obtiene todos los empleados almacenados en la base de datos
    employees = Employee.objects.select_related('idsubarea__idarea').all()
    # Pasa los datos al contexto y renderiza la plantilla
    context = {
        'employees': employees,
    }
    return render(request, 'api/ver_employee.html', context)

def update_employee(request, employee_id):
    # Obtiene el objeto Employee que deseas actualizar
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        # Si la solicitud es un POST, procesa el formulario y actualiza el empleado
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirige a la página 'ver_employee' después de una actualización exitosa
            return redirect('ver_employee')
        else:
            return render(request, 'api/update_employee.html', {'form': form, 'employee': employee})
    else:
        # Si la solicitud es GET, renderiza el formulario para que el usuario lo complete
        form = EmployeeUpdateForm(instance=employee)
        return render(request, 'api/update_employee.html', {'form': form, 'employee': employee})