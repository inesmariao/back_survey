from django.contrib import admin
from .models import CapituloI, Pais, Nacionalidad

# Registra los modelos en el administrador
admin.site.register(CapituloI)
admin.site.register(Pais)
admin.site.register(Nacionalidad)
