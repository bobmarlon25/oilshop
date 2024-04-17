from django.shortcuts import render, get_object_or_404

from .models import Categoria,Producto
# Create your views here.
""" VISTAS PARA EL CATALOGO DE PRODUCTOS"""

def index(request):
    listaproductos = Producto.objects.all()    
    listacategorias = Categoria.objects.all()   
    contex = {
        'productos':listaproductos,
        'categorias':listacategorias
    }
    return render(request,"index.html",contex)


def productosporcategorias(request,categoria_id):
    """vista para filtrar productos por categoria """
    objcategoria =Categoria.objects.get(pk=categoria_id)
    listaproductos=objcategoria.producto_set.all()
    listacategorias = Categoria.objects.all()  
    context={
        'productos':listaproductos,
        'categorias':listacategorias

    }
    return render(request,"index.html",context)

def productospornombre(request):
    nombre=request.POST['nombre']
    listaproductos=Producto.objects.filter(nombre__contains=nombre)
    listacategorias = Categoria.objects.all()  

    context={
        'productos':listaproductos,
        'categorias':listacategorias

    }
    return render(request,"index.html",context)



def productodetalle(request,producto_id):
    # listaproducto=Producto.objects.get(pk=producto_id)
    listaproducto=get_object_or_404(Producto,pk=producto_id)
    context={
        'producto':listaproducto
    
    }
    return render(request,"producto.html",context)

   
  

