from django import forms
from .models import Branch, ServiceArea, Module

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'address', 'telephone', 'email', 'mobile', 'agent_count', 'email_enabled']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la sede'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# Teléfonico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Dirección correo electrónico'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# Móvil'}),
            'agent_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ServiceAreaForm(forms.ModelForm):
    class Meta:
        model = ServiceArea
        fields = ['branch', 'name', 'description', 'service_letter', 'is_active', 'desks', 'waiting_time_sla', 'serving_time_sla', 'duration']
        

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['branch', 'name', 'description', 'is_active']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione sucursal'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del módulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'is_active': forms.Select(choices=[(True, 'Sí'), (False, 'No')], attrs={'class': 'form-control'}),
        }


class BranchSelectForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), label="Select Branch", empty_label="Choose...")