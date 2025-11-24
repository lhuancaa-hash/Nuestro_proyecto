from django.shortcuts import render, redirect, get_object_or_404
from .models import MovimientoStock
from .forms import MovimientoStockForm
from .models import Producto
from .forms import ProductoForm

def listar_movimientos(request):
    movimientos = MovimientoStock.objects.all().order_by('id_mov')
    return render(request, 'listar_modstock.html', {'movimientos': movimientos})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_movimientos')
    else:
        form = MovimientoStockForm()
    return render(request, 'formulario_modstock.html', {'form': form, 'titulo': 'Crear Movimiento'})

def modificar_movimiento(request, id):
    movimiento = get_object_or_404(MovimientoStock, id_mov=id)
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            return redirect('listar_movimientos')
    else:
        form = MovimientoStockForm(instance=movimiento)
    return render(request, 'modificar_modstock.html', {'form': form, 'movimiento': movimiento})

def eliminar_movimiento(request, id):
    movimiento = get_object_or_404(MovimientoStock, id_mov=id)
    if request.method == 'POST':
        movimiento.delete()
        return redirect('listar_movimientos')
    return redirect('listar_movimientos')

def listar_productos(request):
    productos = Producto.objects.all().order_by('id_prod')
    return render(request, 'listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id_prod=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'modificar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id_prod=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return redirect('listar_productos')
