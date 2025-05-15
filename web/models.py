from django.db import models 
import uuid
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

#(carro ,moto )
class vehiculo (models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

#(motul shell)
class Marcas(models.Model):
    nombre =models.CharField(max_length=200)
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

#(gasolina , acpm )
class combustible (models.Model):
    nombre =models.CharField(max_length=200)
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
#(20 w 20 ) 
class referencia (models.Model):
    nombre =models.CharField(max_length=200)
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    
#( sintetico, valvulina ) 
class tipo (models.Model):
    nombre =models.CharField(max_length=200)
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    vehiculo = models.ForeignKey(vehiculo,on_delete=models.RESTRICT)
    marca= models.ForeignKey(Marcas,on_delete=models.RESTRICT)
    combustible=models.ForeignKey(combustible,on_delete=models.RESTRICT)
    referencia=models.ForeignKey(referencia,on_delete=models.RESTRICT)
    tipo=models.ForeignKey(tipo,on_delete=models.RESTRICT)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField(null=True)
    precio=models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    imagen = CloudinaryField('imagen')  # Campo de imagen usando Cloudinary
    
    
    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.RESTRICT)
    cc=models.CharField(max_length=10)
    sexo=models.CharField(max_length=1,default='m')
    telefono= models.CharField(max_length=15)
    fecha_nacimiento= models.DateField(null=True)
    direccion=models.TextField()

    def __srt__(self):
        return self.cc
    

class Pedido(models.Model):
    ESTADO_CHOICES=(
        ('0','SOLICITADO'),
        ('1','PAGADO')
    )
    cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=20, blank=True, null=True, unique=True)
    monto_total=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado=models.CharField(max_length=1,default=0,choices=ESTADO_CHOICES)


    def __srt__(self):
        return self.nro_pedido
    

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.producto.nombre




