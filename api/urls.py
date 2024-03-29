from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new_employee/', views.new_employee, name='new_employee'),
    path('ver_employee/', views.ver_employee, name='ver_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name="delete_employee"),
    
]