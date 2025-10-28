from django import forms
from .models import Venta, Cliente, Producto

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'productos']
        widgets = {
            'productos': forms.CheckboxSelectMultiple,
        }
