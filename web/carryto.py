class Cart():
    def __init__(self, request):
        self.request=request  # para crear un tipo requesd 
        self.session=request.session # obtiene la seccion del navegador 
        

        cart=self.session.get("cart")
        monto=self.session.get("montototal")
        if not cart:
            cart=self.session['cart']={}
            monto=self.session['montototal']= "0"

        self.cart=cart  
        self.monto=float(monto)

    def add(self,producto,cantidad):
        if str(producto.id) not in self.cart.keys(): # para revisar si ya existe el producto en carrito 
            self.cart[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "cantidad":cantidad,
                "precio":str(producto.precio),
                "imagen": producto.imagen.url if producto.imagen else "https://placehold.co/250",
                "vehiculo":producto.vehiculo.nombre,
                "subtotal":str(cantidad*producto.precio)
            }
        else:
            # actualizamos el producto en el carrito 
            for key,value in self.cart.items():
                if key ==str(producto.id):
                    value["cantidad"]=str(int(value["cantidad"])+ cantidad)
                    value["subtotal"]=str(float(value["cantidad"])*float(value["precio"]))
                    break


        self.save()

    def delete(self,producto):
        producto_id=str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()


    def clear(self):
        self.session["cart"]={}
        self.session["montototal"]="0"

    def save(self): 
        """"guarda cambios en el carrito de compras """
        monto=0
        for key,value in self.cart.items():
            monto +=float(value["subtotal"])

        
        self.session["montototal"]=monto
        self.session["cart"]=self.cart
        self.session.modified= True


