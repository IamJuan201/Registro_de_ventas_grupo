#REGISTRO DE VENTAS
print("Bienvenido/a, ¡gracias, por preferirnos al comprar!")

nombre_del_cliente = input("Nombre del cliente: ")

while True:     
    nombre_del_producto = input("Nombre del producto: ")
    cantidad = int(input("ingrese la cantidades del producto: "))
    precio = float(input("ingrese el valor unitario del producto: "))

    sub_total= cantidad * precio 
    print(f"hola {nombre_del_cliente}, su cuenta va: {sub_total}")
 
    continuar = input("¿Desea agregar otro producto? (si/no): ").lower()
    
    if continuar == "no":
        break   # rompe el ciclo
    

    
   


