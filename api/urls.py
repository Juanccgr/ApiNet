from django.urls import path
from .views import EmployeeListView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new_employee/', views.new_employee, name='new_employee'),
    path('ver_employee/', EmployeeListView.as_view(), name='ver_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name="delete_employee"),
    path('edit_employee/<int:id>', views.edit_employee, name="edit_employee"),
    
]