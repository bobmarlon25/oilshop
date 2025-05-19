from django.contrib import admin
from .models import Tipo, Producto, Vehiculo, Marcas, Combustible, Referencia
# Register your models here.
admin.site.register(Tipo)
admin.site.register(Referencia)
admin.site.register(Vehiculo)
admin.site.register(Marcas)
admin.site.register(Combustible)


@admin.register(Producto) # DECORADOR
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','tipo','marca','vehiculo') 
    list_editable=('precio',)