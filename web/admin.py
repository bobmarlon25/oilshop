from django.contrib import admin
from .models import Categoria,Producto,Vehiculo,Marcas 
# Register your models here.
admin.site.register(Categoria)
# admin.site.register(Producto)
admin.site.register(Vehiculo)
admin.site.register(Marcas)

@admin.register(Producto) # DECORADOR
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','categoria','marca','vehiculo') 
    list_editable=('precio',)