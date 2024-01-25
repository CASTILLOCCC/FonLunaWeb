from django.contrib import admin
from .models import asociados
from .models import tipoasociados
from .models import aportes

admin.site.register(asociados)
admin.site.register(tipoasociados)
admin.site.register(aportes)
