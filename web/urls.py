
from django.urls import path

from . import views 

app_name='web'



urlpatterns = [
    path('',views.index,name='index'),
    path('productosporcategorias/<int:categoria_id>',views.productosporcategorias,name='productosporcategorias'),
    path('productospornombre',views.productospornombre,name='productospornombre'),
    path('producto/<int:producto_id>',views.productodetalle, name='producto')
]