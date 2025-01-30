
from django.urls import path

from . import views 

app_name='web'



urlpatterns = [
    path('',views.index,name='index'),
    path('productosporcategorias/<int:categoria_id>',views.productosporcategorias,name='productosporcategorias'),
    path('productospormarcas/<int:marcas_id>',views.productospormarcas,name='productospormarcas'),
    path('productosporcombustible/<int:combustible_id>',views.productosporcombustible,name='productosporcombustible'),
    path('productosporreferencia/<int:referencia_id>',views.productosporreferencia,name='productosporreferencia'),
    path('productosportipo/<int:tipo_id>',views.productosportipo,name='productosportipo'),
    path('productospornombre',views.productospornombre,name='productospornombre'),
   # path('producto/<int:producto_id>',views.productodetalle, name='producto'),
    path('producto/<int:producto_id>',views.productodetalle, name='producto'),
    # path('carrito',views.carrito,name='carrito'),

    # path('agregarcarrito/<int:producto_id>',views.agregarcarrito,name='agregarcarrito'),
    # path('agregarcarrito_/<int:producto_id>',views.agregarcarrito_,name='agregarcarrito_'),
    # path('limpiarcarrito',views.limpiarcarrito,name='limpiarcarrito'),
    # path('eliminarproducto/<int:producto_id>',views.eliminarproducto,name='eliminarproducto')
]