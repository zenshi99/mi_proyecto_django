from django.urls import path
from . import views

urlpatterns = [
    path('venta/', views.registrar_venta, name='registrar_venta'),
    path('venta-exitosa/', views.venta_exitosa, name='venta_exitosa'),
]
