from django.urls import path
from . import views

urlpatterns = [
    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/modificar/<int:id>/', views.modificar_movimiento, name='modificar_movimiento'),
    path('movimientos/eliminar/<int:id>/', views.eliminar_movimiento, name='eliminar_movimiento'),
]