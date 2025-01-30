from django.db import models

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
    imagen=models.ImageField(upload_to='productos',blank=True)
    
    def __str__(self):
        return self.nombre