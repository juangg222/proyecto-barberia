from django.contrib import admin
from .models import Barbero, Servicio, Formulario, Cita, Pago
# Register your models here.
admin.site.register(Barbero)
admin.site.register(Servicio)
admin.site.register(Formulario)
admin.site.register(Cita)
admin.site.register(Pago)