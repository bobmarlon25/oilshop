from django.shortcuts import render, get_object_or_404,redirect

from .models import vehiculo,Producto

from .carryto import Cart
# Create your views here.
""" VISTAS PARA EL CATALOGO DE PRODUCTOS"""

def index(request):
    listaproductos = Producto.objects.all()    
    listacategorias = vehiculo.objects.all()   
    contex = {
        'productos':listaproductos,
        'categorias':listacategorias
    }
    return render(request,"index.html",contex)


# def productosporcategorias(request,categoria_id):
#     """vista para filtrar productos por categoria """
#     objcategoria =vehiculo.objects.get(pk=categoria_id)
#     listaproductos=objcategoria.producto_set.all()
#     listacategorias = vehiculo.objects.all()  
#     context={
#         'productos':listaproductos,
#         'categorias':listacategorias

#     }
#     return render(request,"index.html",context)

# def productospornombre(request):
#     nombre=request.POST['nombre']
#     listaproductos=Producto.objects.filter(nombre__contains=nombre)
#     listacategorias = vehiculo.objects.all()  

#     context={
#         'productos':listaproductos,
#         'categorias':listacategorias

#     }
#     return render(request,"index.html",context)



# def productodetalle(request,producto_id):
#     # listaproducto=Producto.objects.get(pk=producto_id)
#     listaproducto=get_object_or_404(Producto,pk=producto_id)
#     context={
#         'producto':listaproducto
    
#     }
#     return render(request,"producto.html",context)

   
# """  vistas para el carrito de compras """

# def carrito(request):
#     return render(request,"carrito.html")



# def agregarcarrito(request,producto_id):
#     if request.method=='POST':
#         cantidad=int(request.POST['cantidad'])

#     else:
#         cantidad=1


#     objproducto=Producto.objects.get(pk=producto_id)
#     carritoproducto = Cart(request)
#     carritoproducto.add(objproducto,cantidad)
    

#     return render(request,"carrito.html")

# def eliminarproducto(request,producto_id):
#     objproducto=Producto.objects.get(pk=producto_id)
#     carritoproducto=Cart(request)
#     carritoproducto.delete(objproducto)

#     return render(request,"carrito.html")
    

# def limpiarcarrito(request):

#     carritoproducto=Cart(request)
#     carritoproducto.clear()

#     return render(request,"carrito.html")
       

# def agregarcarrito_(request,producto_id):
#     if request.method=='POST':
#         cantidad=int(request.POST['cantidad'])

#     else:
#         cantidad=1


#     objproducto=Producto.objects.get(pk=producto_id)
#     carritoproducto = Cart(request)
#     carritoproducto.add(objproducto,cantidad)
    

#     return redirect("/")