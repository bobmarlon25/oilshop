from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# (carro ,moto )
class Vehiculo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("web:filtrar_productos", args=["categoria" , self.id])

# (motul shell)
class Marcas(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("web:filtrar_productos", args=["marca" , self.id])

# (gasolina , acpm )
class Combustible(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("web:filtrar_productos", args=["combustible" , self.id])

# (20 w 20 )
class Referencia(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("web:filtrar_productos", args=["referencia" , self.id])

# ( sintetico, valvulina )
class Tipo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("web:filtrar_productos", args=["tipo" , self.id])

class Producto(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT)
    marca = models.ForeignKey(Marcas, on_delete=models.RESTRICT)
    combustible = models.ForeignKey(Combustible, on_delete=models.RESTRICT)
    referencia = models.ForeignKey(Referencia, on_delete=models.RESTRICT)
    tipo = models.ForeignKey(Tipo, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = CloudinaryField("imagen")  # Campo de imagen usando Cloudinary

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    cc = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1, default="m")
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    def __srt__(self):
        return self.cc


class Pedido(models.Model):
    ESTADO_CHOICES = (("0", "SOLICITADO"), ("1", "PAGADO"))
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=20, blank=True, null=True, unique=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=1, default=0, choices=ESTADO_CHOICES)

    def __srt__(self):
        return self.nro_pedido


class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre
