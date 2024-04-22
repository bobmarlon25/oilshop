
from django.urls import path

from . import views 

app_name='web'



urlpatterns = [
    path('',views.index,name='index'),
    path('productosporcategorias/<int:categoria_id>',views.productosporcategorias,name='productosporcategorias'),
    path('productospornombre',views.productospornombre,name='productospornombre'),
    path('producto/<int:producto_id>',views.productodetalle, name='producto'),
    path('carrito',views.carrito,name='carrito'),

    path('agregarcarrito/<int:producto_id>',views.agregarcarrito,name='agregarcarrito'),
    path('agregarcarrito_/<int:producto_id>',views.agregarcarrito_,name='agregarcarrito_'),
    path('limpiarcarrito',views.limpiarcarrito,name='limpiarcarrito'),
    path('eliminarproducto/<int:producto_id>',views.eliminarproducto,name='eliminarproducto')
]