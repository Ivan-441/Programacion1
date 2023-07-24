from django.urls import path
from .import views

urlpatterns = [
    path('', views.clientes, name='clientes'),

    path('actividades', views.actividades, name='actividades'),
    path('registrarActividad/', views.registrarActividad, name='registarActividad'),
    path('eliminarActividad/<codigo>', views.eliminarActividad, name='eliminarActividad'),

    path('pagos', views.pagos, name='pagos'),
    path('registrarPago/', views.registrarPago, name='registarPago'),
    path('eliminarPago/<id>', views.eliminarPago, name='eliminarPago'),

    path('inscripciones', views.inscripciones, name='inscripciones'),
    path('eliminarInscripcion/<actividad>/<dni_cliente>', views.eliminarInscripcion, name='eliminarInscripcion'),
    path('registrarInscripcion/', views.registrarInscripcion, name='registarInscripcion'),
    

    path('registrarCliente/', views.registrarCliente, name='registarCliente'),
    path('eliminarCliente/<dni>', views.eliminarCliente, name='eliminarCliente'),
    path('edicionCliente/<dni>', views.edicionCliente, name='edicionCliente'),
    path('editarCliente/', views.editarCliente, name='editarCliente'),
]
