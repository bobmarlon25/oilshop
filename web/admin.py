from django.contrib import admin
from .models import Categoria,Producto
# Register your models here.
admin.site.register(Categoria)
# admin.site.register(Producto)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','categoria') 
    list_editable=('precio',)