from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_minimo = models.IntegerField(default=5)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'

class MovimientoStock(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"

    class Meta:
        db_table = 'movimiento_stock'