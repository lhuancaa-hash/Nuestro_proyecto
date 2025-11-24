from django import forms
from .models import MovimientoStock
from .models import Producto

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
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio_compra', 'precio_venta', 'unidad_medida', 'id_prov']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'id_prov': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio_compra': 'Precio de Compra',
            'precio_venta': 'Precio de Venta',
            'unidad_medida': 'Unidad de Medida',
            'id_prov': 'Proveedor',
        }
