from django import forms
from django.forms import TextInput

from .models import *


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['namecountry']
    widgets = {
            'namecountry': TextInput(attrs={'class': 'form-control'}),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['namearea']
        widgets = {
            'namearea': TextInput(attrs={'class': 'form-control'}),
        }

class SubareaForm(forms.ModelForm):
    class Meta:
        model = Subarea
        fields = ['namesubarea']
        widgets = {
            'namesubarea': TextInput(attrs={'class': 'form-control'}),
        }

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['nametype']
        widgets = {
            'nametype': TextInput(attrs={'class': 'form-control'}),

        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'documentnumber', 'datehirirng', 'idsubarea', 'iddocumenttype']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'documentnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'datehirirng': forms.DateInput(attrs={'class': 'form-control'}),
            'idsubarea': forms.Select(attrs={'class': 'form-control'}),
            'iddocumenttype': forms.Select(attrs={'class': 'form-control'}),
            'idarea': forms.Select(attrs={'class': 'form-control'}),
            'idcountry': forms.Select(attrs={'class': 'form-control'}),
        }
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'documentnumber', 'idsubarea']