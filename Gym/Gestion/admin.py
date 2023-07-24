from django.contrib import admin
from .models import Cliente, Pago, Inscripcion, Actividad
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Inscripcion)
admin.site.register(Actividad)