from django.shortcuts import render, redirect, get_object_or_404
from .models import MovimientoStock
from .forms import MovimientoStockForm
from .models import Stock
from .forms import StockForm

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
# ====== CRUD STOCK ============
# READ
def listar_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'listar_stock.html', {'stocks': stocks})
# CREATE
def crear_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_stock')
    else:
        form = StockForm()
    return render(request, 'formulario_stock.html', {'form': form, 'titulo': 'Crear Stock'})
#M MODIFICAR
def modificar_stock(request, id):
    stock = get_object_or_404(Stock, id_stock=id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('listar_stock')
    else:
        form = StockForm(instance=stock)
    return render(request, 'formulario_stock.html', {'form': form, 'stock': stock})
# ELIMINAR 
def eliminar_stock(request, id):
    stock = get_object_or_404(Stock, id_stock=id)
    if request.method == 'POST':
        stock.delete()
        return redirect('listar_stock')
    return redirect('listar_stock')