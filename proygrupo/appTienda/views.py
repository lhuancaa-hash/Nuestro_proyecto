from django.shortcuts import render, redirect, get_object_or_404
from .models import MovimientoStock
from .forms import MovimientoStockForm
from .models import Stock
from .forms import StockForm
from django.db.models import F
from django.contrib import messages
from .forms import BuscarProveedorForm
from .forms import FiltrarMovimientosForm
from .models import Producto
from .forms import ProductoForm
from .forms import BuscarProveedorForm
from .forms import BuscarMovimientosDiaForm
from django.utils import timezone
from django.db.models import Sum
from django.db.models import FloatField


def lista_valor_productos(request):
    # Consulta: traer todos los stocks con info del producto
    stocks = Stock.objects.annotate(
        valor_total=F('cantidad') * F('id_prod__precio_compra')
    )

    # Calcular el valor total de todo el inventario
    valor_inventario_total = stocks.aggregate(
        total=Sum('valor_total', output_field=FloatField())
    )['total'] or 0

    context = {
        'stocks': stocks,
        'valor_inventario_total': valor_inventario_total,
    }
    return render(request, 'valor_productos.html', context)

#-----Para empleado
def listar_stock_emp(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_emp.html', {'stocks': stocks})

def listar_productos_emp(request):
    productos = Producto.objects.all().order_by('id_prod')
    return render(request, 'productos_emp.html', {'productos': productos})

def listar_movimientos_emp(request):
    movimientos = MovimientoStock.objects.all().order_by('id_mov')
    return render(request, 'mov_emp.html', {'movimientos': movimientos})


def movimientos_dia(request):
    movimientos = []
    form = BuscarMovimientosDiaForm(request.GET or None)

    if form.is_valid():
        fecha = form.cleaned_data['fecha']

        # Convertimos la fecha a rango de inicio y fin del día
        inicio = timezone.make_aware(timezone.datetime.combine(fecha, timezone.datetime.min.time()))
        fin = timezone.make_aware(timezone.datetime.combine(fecha, timezone.datetime.max.time()))

        movimientos = MovimientoStock.objects.filter(fecha__range=(inicio, fin)).order_by('-fecha')

    return render(request, 'movimientos_dia.html', {
        'form': form,
        'movimientos': movimientos,
        'fecha_seleccionada': form.cleaned_data['fecha'] if form.is_valid() else None
    })


def historial_movimientos(request):
    movimientos = []
    form = FiltrarMovimientosForm(request.GET or None)  # usamos GET para poder compartir URL

    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']

        movimientos = MovimientoStock.objects.filter(
            fecha__gte=fecha_inicio,
            fecha__lte=fecha_fin
        ).order_by('-fecha')

    return render(request, 'historial_movimientos.html', {
        'form': form,
        'movimientos': movimientos
    })


def buscar_proveedor(request):
    if request.method == 'POST':
        form = BuscarProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.cleaned_data['proveedor']
            # Redirigimos a la página de productos de ese proveedor
            return redirect('productos_proveedor', id_prov=proveedor.id_prov)
    else:
        form = BuscarProveedorForm()

    return render(request, 'buscar_proveedor.html', {'form': form})

def productos_proveedor(request, id_prov):
    productos = Producto.objects.filter(id_prov_id=id_prov)
    return render(request, 'productos_proveedor.html', {'productos': productos})


def pagina_principal(request):
    # Traer todos los stocks con cantidad <= stock_minimo
    stocks_criticos = Stock.objects.filter(cantidad__lte=F('stock_minimo'))
    # VALOR TOTAL DEL INVENTARIO (usando precio_compra)
    valor_inventario = Stock.objects.aggregate(
        total=Sum(F('cantidad') * F('id_prod__precio_compra'))
    )['total'] or 0

    productos_bajos = Stock.objects.filter(cantidad__lt=F('stock_minimo')).count()
    productos_agotados = Stock.objects.filter(cantidad=0).count()
    total_productos = Producto.objects.count()
    context = {
        'stocks_criticos': stocks_criticos,
        # otros contextos que ya tengas
        'valor_inventario': valor_inventario,
        'productos_bajos': productos_bajos,
        'productos_agotados': productos_agotados,
        'total_productos': total_productos,
    }
    

    return render(request, 'principal.html', context)



#-------------------------------
def listar_movimientos(request):
    movimientos = MovimientoStock.objects.all().order_by('id_mov')
    return render(request, 'listar_modstock.html', {'movimientos': movimientos})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Movimiento registrado correctamente.")
                return redirect('listar_movimientos')

            except Exception as e:

                mensaje = str(e)

                # Detectamos el mensaje del modelo
                if "STOCK_INSUFICIENTE" in mensaje:
                    stock_disponible = mensaje.split(":")[1]
                    messages.error(
                        request, 
                        f"❌ Stock insuficiente. Stock actual disponible: {stock_disponible}."
                    )
                else:
                    messages.error(request, "Ocurrió un error al registrar el movimiento.")

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
# ====== CRUD PROVEEDOR ============
from .models import Proveedor
from .forms import ProveedorForm
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    print(">>> VISTA EJECUTADA <<<")
    return render(request, 'lista_prov.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'crear_prov.html', {'form': form})  # FIX

def actualizar_proveedor(request, id_prov):
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'actualizar_prov.html', {'form': form})  # FIX

def eliminar_proveedor(request, id_prov):
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    proveedor.delete()
    return redirect('lista_proveedores')



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