from django import forms
from .models import MovimientoStock

class MovimientoStockForm(forms.ModelForm):
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1'
        }),
        label='Cantidad'
    )
    
    class Meta:
        model = MovimientoStock
        fields = ['producto', 'tipo', 'cantidad', 'ubicacion', 'descripcion']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Motivo del movimiento...'}),
        }
        labels = {
            'producto': 'Producto',
            'tipo': 'Tipo de Movimiento',
            'cantidad': 'Cantidad',
            'ubicacion': 'Ubicación',
            'descripcion': 'Descripción/Motivo',
        }