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
        fields = ['id_prod', 'tipo', 'cantidad', 'usuario', 'motivo']
        widgets = {
            'id_prod': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del usuario...'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Motivo del movimiento...'}),
        }
        labels = {
            'id_prod': 'Producto',
            'tipo': 'Tipo de Movimiento',
            'cantidad': 'Cantidad',
            'usuario': 'Usuario',
            'motivo': 'Motivo',
        }