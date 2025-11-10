from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),                       # ✅ INICIO
    path('habitacion/agregar/', views.agregar_habitacion, name='agregar_habitacion'),
    path('habitacion/ver/', views.ver_habitaciones, name='ver_habitaciones'),
    path('habitacion/actualizar/<int:id>/', views.actualizar_habitacion, name='actualizar_habitacion'),
    path('habitacion/borrar/<int:id>/', views.borrar_habitacion, name='borrar_habitacion'),
]
