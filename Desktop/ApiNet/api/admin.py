from django.contrib import admin
from .models import Country, Area, Subarea, DocumentType, Employee
# Register your models here.

admin.site.register(Country)
admin.site.register(Area)
admin.site.register(Subarea)
admin.site.register(DocumentType)
admin.site.register(Employee)