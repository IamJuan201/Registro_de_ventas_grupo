#REGISTRO DE VENTAS
print("Bienvenido/a, ¡gracias, por preferirnos al comprar!")
nombre_del_cliente = input("Nombre del cliente: ")
nombre_del_producto = input("Nombre del producto: ")
cantidad = int(input("ingrese la cantidades del producto: "))
precio = float(input("ingrese el valor unitario del producto: "))

sub_total= cantidad * precio 
iva = sub_total * 0.19
total_de_venta = sub_total + iva
print(f"hola {nombre_del_cliente}, su total es: {total_de_venta} ¡gracias por su compra!")


