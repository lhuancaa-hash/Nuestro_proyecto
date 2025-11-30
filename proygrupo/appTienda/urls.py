from django.urls import path
from . import views

urlpatterns = [
    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/modificar/<int:id>/', views.modificar_movimiento, name='modificar_movimiento'),
    path('movimientos/eliminar/<int:id>/', views.eliminar_movimiento, name='eliminar_movimiento'),
    path('stock/', views.listar_stock, name='listar_stock'),
    path('stock/crear/', views.crear_stock, name='crear_stock'),
    path('stock/modificar/<int:id>/', views.modificar_stock, name='modificar_stock'),
    path('stock/eliminar/<int:id>/', views.eliminar_stock, name='eliminar_stock'),   
    path('proveedor/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedor/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/actualizar/<int:id_prov>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/eliminar/<int:id_prov>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('pagina_principal/', views.pagina_principal,name='pagina_principal'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/modificar/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('buscar-proveedor/', views.buscar_proveedor, name='buscar_proveedor'),
    path('productos-proveedor/<int:id_prov>/', views.productos_proveedor, name='productos_proveedor'),
    path('historial-movimientos/', views.historial_movimientos, name='historial_movimientos'),
    path('movimientos-dia/', views.movimientos_dia, name='movimientos_dia'),
    path('movimientos_emp',views.listar_movimientos_emp, name='listar_movimientos_emp'),
    path('productos_emp',views.listar_productos_emp,name='listar_productos_emp'),
    path('stock_emp',views.listar_stock_emp,name='listar_stock_emp'),
    path('valor_productos',views.lista_valor_productos,name='lista_valor_productos')
]