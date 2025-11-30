from django.db import models
from django.core.validators import MinValueValidator
from django import forms
class Proveedor(models.Model):
    id_prov = models.AutoField(primary_key=True, db_column='id_prov')
    nombre = models.CharField(max_length=100, db_column='nombre')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='telefono')
    direccion = models.CharField(max_length=200, blank=True, null=True, db_column='direccion')
    rubro = models.CharField(max_length=80, blank=True, null=True, db_column='rubro')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedor'

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True, db_column='id_prod')
    nombre = models.CharField(max_length=150, db_column='nombre')
    categoria = models.CharField(max_length=50, blank=True, null=True, db_column='categoria')
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_column='precio_compra')
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_column='precio_venta')
    unidad_medida = models.CharField(max_length=50, blank=True, null=True, db_column='unidad_medida')
    id_prov = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_prov')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'

class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True, db_column='id_stock')
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_prod')
    cantidad = models.IntegerField(default=0, db_column='cantidad')
    ubicacion = models.CharField(max_length=100, blank=True, null=True, db_column='ubicacion')
    stock_minimo = models.IntegerField(default=0, db_column='stock_minimo')

    def __str__(self):
        return f"{self.id_prod.nombre} - {self.ubicacion}"

    class Meta:
        db_table = 'stock'

class MovimientoStock(models.Model):
    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Salida'),
    ]
    
    id_mov = models.AutoField(primary_key=True, db_column='id_mov')
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_prod')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, db_column='tipo')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)], db_column='cantidad')
    fecha = models.DateTimeField(auto_now_add=True, db_column='fecha')
    usuario = models.CharField(max_length=100, blank=True, null=True, db_column='usuario')
    motivo = models.CharField(max_length=200, blank=True, null=True, db_column='motivo')

    def save(self, *args, **kwargs):

        # Obtener el stock asociado al producto
        try:
            stock = Stock.objects.get(id_prod=self.id_prod)
        except Stock.DoesNotExist:
            raise ValueError("No existe un registro de stock para este producto.")

        # Solo modificar stock si es un nuevo movimiento
        if not self.pk:
            if self.tipo == 'E':  # Entrada
                stock.cantidad += self.cantidad
            elif self.tipo == 'S':  # Salida
                if stock.cantidad < self.cantidad:
                    # Indica a la vista que el stock es insuficiente
                    raise ValueError(f"STOCK_INSUFICIENTE:{stock.cantidad}")
                stock.cantidad -= self.cantidad

            stock.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.id_prod.nombre} - {self.cantidad}"

    class Meta:
        db_table = 'movimiento_stock'

class BuscarProveedorForm(forms.Form):
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        label="Seleccione un proveedor",
        empty_label="--- Seleccione un proveedor ---",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class BuscarMovimientosDiaForm(forms.Form):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Seleccione una fecha"
    )
