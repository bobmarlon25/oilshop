from django.contrib import admin
from .models import tipo,Producto,vehiculo,Marcas ,combustible,referencia
# Register your models here.
admin.site.register(tipo)
admin.site.register(referencia)
admin.site.register(vehiculo)
admin.site.register(Marcas)
admin.site.register(combustible)


@admin.register(Producto) # DECORADOR
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','tipo','marca','vehiculo') 
    list_editable=('precio',)