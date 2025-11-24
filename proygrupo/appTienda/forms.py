from django import forms
from .models import MovimientoStock
from .models import Stock

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

class StockForm(forms.ModelForm):
    cantidad = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0'
        }),
        label='Cantidad'
    )
    
    stock_minimo = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0'
        }),
        label='Stock mínimo'
    )

    class Meta:
        model = Stock
        fields = ['id_prod', 'cantidad', 'ubicacion', 'stock_minimo']
        widgets = {
            'id_prod': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación del stock...'}),
        }
        labels = {
            'id_prod': 'Producto',
            'cantidad': 'Cantidad',
            'ubicacion': 'Ubicación',
            'stock_minimo': 'Stock mínimo',
        }