
from django.urls import path

from . import views 

app_name='web'



urlpatterns = [
    path('',views.index,name='index'),
    # remplazando los siguientes path por una unica funcion
    # path('productosporcategorias/<int:categoria_id>',views.productosporcategorias,name='productosporcategorias'),
    # path('productospormarcas/<int:marcas_id>',views.productospormarcas,name='productospormarcas'),
    # path('productosporcombustible/<int:combustible_id>',views.productosporcombustible,name='productosporcombustible'),
    # path('productosporreferencia/<int:referencia_id>',views.productosporreferencia,name='productosporreferencia'),
    # path('productosportipo/<int:tipo_id>',views.productosportipo,name='productosportipo'),
    path('productos/buscar-por/<slug:termino>/<int:termino_id>',views.filtrar_productos, name='filtrar_productos'),

    path('productospornombre',views.productospornombre,name='productospornombre'),
   # path('producto/<int:producto_id>',views.productodetalle, name='producto'),
    path('producto/<int:producto_id>',views.productodetalle, name='producto'),
    path('carrito',views.carrito,name='carrito'),

    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('limpiarcarrito',views.limpiarcarrito,name='limpiarcarrito'),
    path('eliminarproducto/<int:producto_id>',views.eliminarproducto,name='eliminarproducto'),
    path('crearusuario',views.CrearUsuario,name='crearusuario'),
    path('cuenta',views.CuentaUsuario,name='cuenta'),
    path('actualizarcliente',views.actualizarcliente,name='actualizarcliente'),
    path('login',views.loginUsuario,name='login'),
    path('logout',views.logoutUsuario,name='logout'),
    path('registrarpedido',views.registrarPedido,name='registrarpedido'),
    path('pruebapaypal',views.view_that_asks_for_money,name='pruebapaypal'),
    path('confirmarpedido',views.ConfirmarPedido,name='confirmarpedido'),
    path('gracias',views.gracias,name='gracias')
]