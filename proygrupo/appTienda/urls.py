from django.urls import path
from . import views

urlpatterns = [
    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/modificar/<int:id>/', views.modificar_movimiento, name='modificar_movimiento'),
    path('movimientos/eliminar/<int:id>/', views.eliminar_movimiento, name='eliminar_movimiento'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/modificar/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
