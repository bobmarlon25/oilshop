from django.shortcuts import render, get_object_or_404,redirect

from .models import vehiculo,Producto,Marcas,combustible,referencia,tipo,Cliente,Pedido,PedidoDetalle

from .carryto import Cart
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
""" VISTAS PARA EL CATALOGO DE PRODUCTOS"""

def index(request):
    listaproductos = Producto.objects.all()    
    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    contex = {
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo
    }
    
    return render(request,"index.html",contex)


def productosporcategorias(request,categoria_id):
    """vista para filtrar productos por categoria """
    objcategoria =vehiculo.objects.get(pk=categoria_id)
    listaproductos=objcategoria.producto_set.all()
    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

def productospormarcas(request,marcas_id):
    """vista para filtrar productos por categoria """
    objcategoria =Marcas.objects.get(pk=marcas_id)
    listaproductos=objcategoria.producto_set.all()
    
    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

def productosporcombustible(request,combustible_id):
    """vista para filtrar productos por categoria """
    objcategoria =combustible.objects.get(pk=combustible_id)
    listaproductos=objcategoria.producto_set.all()

    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)


def productosporreferencia(request,referencia_id):
    """vista para filtrar productos por categoria """
    objcategoria =referencia.objects.get(pk=referencia_id)
    listaproductos=objcategoria.producto_set.all()

    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)


def productosportipo(request,tipo_id):
    """vista para filtrar productos por categoria """
    objcategoria =tipo.objects.get(pk=tipo_id)
    listaproductos=objcategoria.producto_set.all()
    
    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)



def productospornombre(request):
    nombre=request.POST['nombre']
    listaproductos=Producto.objects.filter(nombre__icontains=nombre)
    
    listacategorias = vehiculo.objects.all()  

    
    listacategorias = vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= combustible.objects.all() 
    listareferencia= referencia.objects.all() 
    listatipo= tipo.objects.all()

    context = {
        'productos':listaproductos,
        'nombre':nombre,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo
    }    
    return render(request,"index.html",context)



def productodetalle(request,producto_id):
    # listaproducto=Producto.objects.get(pk=producto_id)
    listaproducto=get_object_or_404(Producto,pk=producto_id)
    context={
        'producto':listaproducto
    
    }
    return render(request,"producto.html",context)

   
"""  vistas para el carrito de compras """

def carrito(request):
    return render(request,"carrito.html")



def agregarCarrito(request,producto_id):
    if request.method=='POST':
        cantidad=int(request.POST['cantidad'])
        
        accion = str(request.POST.get('accion'))
        
        
        if accion == 'aumentar':
            cantidad = 1
            
        elif accion == 'disminuir' and cantidad > 1:  # Evitar que la cantidad sea menor que 1
            cantidad = -1
            
        elif accion == 'disminuir' and cantidad == 1:  # Evitar que la cantidad sea menor que 1
            cantidad = 0
            
    else:
        cantidad=1



    objproducto=Producto.objects.get(pk=producto_id)
    carritoproducto = Cart(request)
    carritoproducto.add(objproducto,cantidad)
    if request.method=='GET':
        return redirect("/")
    else:
        return render(request,"carrito.html")

def eliminarproducto(request,producto_id):
    objproducto=Producto.objects.get(pk=producto_id)
    carritoproducto=Cart(request)
    carritoproducto.delete(objproducto)

    return render(request,"carrito.html")
    

def limpiarcarrito(request):

    carritoproducto=Cart(request)
    carritoproducto.clear()

    return render(request,"carrito.html")
       


#####vistas para usuarios ####
from .forms import ClienteForm
def CrearUsuario(request):
    if request.method== 'POST':
        datausuario=request.POST['nuevousuario']
        datapasword=request.POST['nuevopassword']

        nuevoUsuario=User.objects.create_user(username=datausuario,password=datapasword)

        if nuevoUsuario is not None:
            login(request,nuevoUsuario)

            return redirect('/cuenta')

        
    



    return render(request,'login.html')
    

def CuentaUsuario(request):
    
    frmCliente=ClienteForm()
    context={
        'frmcliente':frmCliente
    }
    return render(request,'cuenta.html',context)



def actualizarcliente(request):
    mensaje=" "

    if request.method == 'POST':
        frmCliente=ClienteForm(request.POST)
        if frmCliente.is_valid():
            dataCliente=frmCliente.cleaned_data


            #actualizar usuario 
            actUsuario=User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()


            nuevoCliente = Cliente()
            nuevoCliente.usuario = actUsuario
            nuevoCliente.cc = dataCliente["cc"]
            nuevoCliente.direcion = dataCliente["direccion"]
            nuevoCliente.telefono = dataCliente["telefono"]
            nuevoCliente.sexo = dataCliente["sexo"]
            nuevoCliente.fecha_nacimiento = dataCliente["fecha_nacimiento"]
            nuevoCliente.save()
            context={

            'mensaje':" correctamente se guardo",
            'frmcliente':frmCliente}

    return  render(request,'cuenta.html',context)