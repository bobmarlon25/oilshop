from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from .models import Vehiculo,Producto,Marcas,Combustible,Referencia,Tipo,Cliente,Pedido,PedidoDetalle

from .carryto import Cart
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

""" VISTAS PARA EL CATALOGO DE PRODUCTOS"""

def filtrar_productos(request, termino:str, termino_id:int):
    """
    filtra productos en funcion del termino de busqueda
    devuelve HttpResponse(status=404) si:
    - el **termino** no esta dentro de **CLASES_PARA_TERMINOS_ACEPTADOS_DE_BUSQUEDA**
    - el **termino_id** no corresponde al id de ninguna instancia de la clase buscada 
    """

    CLASES_PARA_TERMINOS_ACEPTADOS_DE_BUSQUEDA = {
        "categoria": Vehiculo,
        "marca": Marcas,
        "combustible": Combustible,
        "referencia": Referencia,
        "tipo": Tipo,
    }
    
    if termino not in CLASES_PARA_TERMINOS_ACEPTADOS_DE_BUSQUEDA:
        raise Http404()

    # obtenemos la clase que usaremos para filtrar los Productos
    ClaseBusqueda = CLASES_PARA_TERMINOS_ACEPTADOS_DE_BUSQUEDA[termino]
    instacia_clase_buscada = get_object_or_404(ClaseBusqueda, pk=termino_id)

    context = {
        "productos": instacia_clase_buscada.producto_set.all(),
        "categorias": Vehiculo.objects.all(),
        "marcas": Marcas.objects.all(),
        "combustibles": Combustible.objects.all(),
        "referencias": Referencia.objects.all(),
        "tipos": Tipo.objects.all(),
    }
    return render(request, "index.html", context)


def index(request):
    listaproductos = Producto.objects.all()    
    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

    contex = {
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustibles': listacombustible,
        'referencias': listareferencia,
        'tipos': listatipo
    }
    
    return render(request,"index.html",contex)

# esta funcion ya no es necesaria y puede eliminada 
def productosporcategorias(request,categoria_id):
    """vista para filtrar productos por categoria """
    objcategoria =Vehiculo.objects.get(pk=categoria_id)
    listaproductos=objcategoria.producto_set.all()
    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

# esta funcion ya no es necesaria y puede eliminada 
def productospormarcas(request,marcas_id):
    """vista para filtrar productos por categoria """
    objcategoria =Marcas.objects.get(pk=marcas_id)
    listaproductos=objcategoria.producto_set.all()
    
    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

# esta funcion ya no es necesaria y puede eliminada 
def productosporcombustible(request,combustible_id):
    """vista para filtrar productos por categoria """
    objcategoria =Combustible.objects.get(pk=combustible_id)
    listaproductos=objcategoria.producto_set.all()

    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

# esta funcion ya no es necesaria y puede eliminada 
def productosporreferencia(request,referencia_id):
    """vista para filtrar productos por categoria """
    objcategoria =Referencia.objects.get(pk=referencia_id)
    listaproductos=objcategoria.producto_set.all()

    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

    context={
        'productos':listaproductos,
        'categorias':listacategorias,
        'marcas': listamarcas,
        'combustible': listacombustible,
        'referencia': listareferencia,
        'tipo': listatipo

    }
    return render(request,"index.html",context)

# esta funcion ya no es necesaria y puede eliminada 
def productosportipo(request,tipo_id):
    """vista para filtrar productos por categoria """
    objcategoria =Tipo.objects.get(pk=tipo_id)
    listaproductos=objcategoria.producto_set.all()
    
    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

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
    
    listacategorias = Vehiculo.objects.all()  

    
    listacategorias = Vehiculo.objects.all()  
    listamarcas= Marcas.objects.all() 
    listacombustible= Combustible.objects.all() 
    listareferencia= Referencia.objects.all() 
    listatipo= Tipo.objects.all()

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

        

        try : 
            validar=User.objects.get(username=datausuario)
            return render(request,'login.html',context={
                'user':validar.username,
                'mensaje':'usuario ya esta creado'
                })
            
             

        except User.DoesNotExist:
            nuevoUsuario=User.objects.create_user(username=datausuario,password=datapasword)
            if nuevoUsuario is not None:
                login(request,nuevoUsuario)

                return redirect('/cuenta')

        
    



    return render(request,'login.html')
    

def CuentaUsuario(request):
    if request.user.is_authenticated:
        try:
            cuenta_editar=Cliente.objects.get(usuario=request.user)
            datacliente={
                'nombre':request.user.first_name,
                'apellidos':request.user.last_name,
                'email':request.user.email,
                'direccion':cuenta_editar.direccion,
                'telefono':cuenta_editar.telefono,
                'cc':cuenta_editar.cc,
                'sexo':cuenta_editar.sexo,
                'fecha_nacimiento':cuenta_editar.fecha_nacimiento
                }
        except :
            datacliente={
                'nombre':request.user.first_name,
                'apellidos':request.user.last_name,
                'email':request.user.email,}
           
    else:
        return redirect('/login')
    

    
    frmCliente=ClienteForm(datacliente)
    context={
            'frmcliente':frmCliente
        }
    return render(request,'cuenta.html',context)



def loginUsuario (request):
    paginadestino= request.GET.get('next',None)

    context={
        'destino':paginadestino,
        'user':'',
        'mensaje':''}
    
    
    
    if request.method== 'POST':
        datausuario=request.POST['usuario']
        datapasword=request.POST['password']
        paginadestino=request.POST['destino']
        print(paginadestino)
        
       
        usuarioAuth=authenticate(request,username=datausuario,password=datapasword)
        if usuarioAuth is not  None:
            login(request, usuarioAuth)

            if paginadestino != 'None':
                return redirect(paginadestino)
            
            try:
                cuenta=Cliente.objects.get(usuario=request.user)
                login(request,usuarioAuth)
                return redirect('/cuenta')             
            except Cliente.DoesNotExist:
                return redirect('/cuenta')    
                
        

        else :
            context={'mensajeError':'usuario o contraseña incorrecta',
                     'user':'',
                     'mensaje':''}
    
        
    
    return render(request,'login.html',context)
                  

def logoutUsuario(request):
    logout(request)
    return render(request,'login.html')



def actualizarcliente(request):
    mensaje=" "

    if request.method == 'POST':
        frmCliente=ClienteForm(request.POST)
        mensaje=" informacion no valida "
        if frmCliente.is_valid():
            dataCliente=frmCliente.cleaned_data


            #actualizar usuario 
            actUsuario=User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()


           
            # Buscar el cliente existente (relacionado al usuario)
            try:
                nuevoCliente = Cliente.objects.get(usuario=actUsuario)
            except Cliente.DoesNotExist:
                nuevoCliente = Cliente()


            nuevoCliente.usuario = actUsuario
            nuevoCliente.cc = dataCliente["cc"]
            nuevoCliente.direccion = dataCliente["direccion"]
            nuevoCliente.telefono = dataCliente["telefono"]
            nuevoCliente.sexo = dataCliente["sexo"]
            nuevoCliente.fecha_nacimiento = dataCliente["fecha_nacimiento"]
            nuevoCliente.save()
            
            mensaje=" correctamente se guardo"
            
            
    context={

    'mensaje':mensaje,
    'frmcliente':frmCliente}

    return  render(request,'cuenta.html',context)

##vistas para proceso de commpras ##
@login_required(login_url='/login')

def registrarPedido(request):

   
    try:
        cuenta_editar=Cliente.objects.get(usuario=request.user)
        datacliente={
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'direccion':cuenta_editar.direccion,
            'telefono':cuenta_editar.telefono,
            'cc':cuenta_editar.cc,
            'sexo':cuenta_editar.sexo,
            'fecha_nacimiento':cuenta_editar.fecha_nacimiento
            }
        
    except :
        datacliente={
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,}
        frmCliente=ClienteForm(datacliente)
        
        context={
            'frmcliente':frmCliente
            }
        return render(request,'cuenta.html',context)
           
    

    
    frmCliente=ClienteForm(datacliente)
    context={
        'frmCliente':frmCliente
    }

    return render(request,'pedido.html',context)


from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "sb-vtv9839986270@business.example.com",
        "amount": "1.00",
        "item_name": "producto prueba ",
        "invoice": "100-ed100",
        "notify_url": request.build_absolute_uri('paypal-ipn'),
        "return": request.build_absolute_uri('/'),  # Asegúrate de tener 'home' en tus urls
        "cancel_return": request.build_absolute_uri('/logout'),  # Igual con 'logout'
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)



@login_required(login_url='/login')

def ConfirmarPedido(request):
    context = {}

    if request.method == "POST":
        # actualizamos datos de usuario
        actUsuario = User.objects.get(pk=request.user.id)
        actUsuario.first_name = request.POST['nombre']
        actUsuario.last_name = request.POST['apellidos']
        actUsuario.save()
        
        # registramos o actualizamos cliente
        try:
            clientePedido = Cliente.objects.get(usuario=request.user)
            clientePedido.telefono =request.POST['telefono']
            clientePedido.direccion=request.POST['direccion']
            clientePedido.save()
        except:
            clientePedido = Cliente()
            clientePedido.usuario=actUsuario
            clientePedido.telefono =request.POST['telefono']
            clientePedido.direccion=request.POST['direccion']
            clientePedido.save()
        
        #registar pedido 
        nropedido=''
        montototal=float(request.session.get('montototal'))
        nuevopedido=Pedido()
        nuevopedido.cliente=clientePedido
        nuevopedido.save()
        
        #actualizar pedidod 
        nropedido='PED'+ nuevopedido.fecha_registro.strftime('%Y') + str(nuevopedido.id)
        nuevopedido.nro_pedido=nropedido
        nuevopedido.monto_total=montototal
        nuevopedido.save()

        #registramos el detalle del pedido
        carritoPedido = request.session.get('cart')

       
        for key, value in carritoPedido.items():
            productoPedido = Producto.objects.get(pk=value['producto_id'])
            detalle = PedidoDetalle()
            detalle.pedido = nuevopedido
            detalle.producto = productoPedido
            detalle.cantidad = int(value['cantidad'])
            detalle.subtotal = float(value['subtotal'])
            detalle.save()

        
       #registar la variable de secion 
        request.session['pedidoId']=nuevopedido.id

        #creamos el boton de paypal 
        paypal_dict = {
        "business": "sb-vtv9839986270@business.example.com",
        "amount": montototal,
        "item_name": "codigo de pedido: "+ nropedido,
        "invoice": nropedido,
        "notify_url": request.build_absolute_uri('paypal-ipn'),
        "return": request.build_absolute_uri('/gracias'),  # Asegúrate de tener 'home' en tus urls
        "cancel_return": request.build_absolute_uri('/logout'),  # Igual con 'logout'
        
    }   
   
        # Create the instance.
        formpaypal = PayPalPaymentsForm(initial=paypal_dict)

        
        context={
            'pedido':nuevopedido,
            'formpaypal':formpaypal
        }

        carrito=Cart(request)
        carrito.clear




    return render(request,'compra.html',context)

from django.core.mail import send_mail

@login_required(login_url='/login')
def gracias(request):
    paypalId = request.GET.get('PayerID', None)
    context ={}
    if paypalId is not None:
        pedidoId = request.session.get('pedidoId')
        pedido = Pedido.objects.get(pk=pedidoId)
        pedido.estado = '1'
        pedido.save()
        context={
            'pedido':pedido
        }

        

        send_mail(
            "GRACIAS POR TU COMPRA",
            "TU NUMERO DE PEDIDO ES "+ pedido.nro_pedido,
            "oilshopabrego@gmail.com",
            [request.user.email,"julianpuentes25@gmail.com"],
            fail_silently=False,
        )
    else:
        return redirect('/')

    return render(request, 'gracias.html',context)

