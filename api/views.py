from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    employees = Employee.objects.select_related('idsubarea__idarea').all()
    document_number = request.GET.get('document_number', '')
    if document_number:
        employees = employees.filter(documentnumber__icontains=document_number)

    empleados_por_pagina = 10

    # Obtiene el número de página desde la solicitud GET
    page = request.GET.get('page', 1)

    paginator = Paginator(employees, empleados_por_pagina)

    try:
        # Obtiene la página solicitada
        employees = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, muestra la primera página
        employees = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, muestra la última página
        employees = paginator.page(paginator.num_pages)

    context = {
        'employees': employees,
    }
    return render(request, 'api/ver_employee.html', context)


def update_employee(request, employee_id):
    # Obtiene el objeto Employee que deseas actualizar
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('ver_employee')
        else:
            return render(request, 'api/update_employee.html', {'form': form, 'employee': employee})
    else:
        form = EmployeeUpdateForm(instance=employee)
        return render(request, 'api/update_employee.html', {'form': form, 'employee': employee})