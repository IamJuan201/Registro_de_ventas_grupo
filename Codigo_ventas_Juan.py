# El codigo VIP es: 1234

import os
NEGRITA = '\033[1m'
RESET = '\033[0m'

while True:
    print(f"{NEGRITA}="*65)
    print("Riwi Tech Store".center(65))
    print("="*65)
    print(f"{RESET}Escriba su nombre:")
    Nombre_del_cliente = input().strip()
    print()
    if Nombre_del_cliente.replace(" ", "").isalpha():
        break
    print("¡ERROR! El nombre solo debe contener letras.")
    print()

while True:
    try:
        print("Escriba la cantidad de productos que desea comprar: ")
        Cantidad_de_Productos =int(input())
        print(f"{NEGRITA}="*65)
        if Cantidad_de_Productos > 0:
            break
        else:
            print("ERROR! La cantidad de productos no puede ser menor o igual a 0")

    except ValueError:
        print("ERROR! Por favor ingrese solo números")
         
Subtotal = 0

for i in range(Cantidad_de_Productos):
    print(f"{NEGRITA}-"*65)
    print(f"{RESET}Producto {i+1}: ")
    
    while True:
        try:
            print("Precio del producto:")
            Precio_Unitario_del_Producto = float(input())
            
            if Precio_Unitario_del_Producto > 0:
                break

            else:
                print("ERROR! El precio del producto no puede ser menor o igual a 0")
            
        except ValueError:
            print("ERROR! Por favor ingrese solo números")
            print()

    while True:
        try:
            print("Cantidad del producto")
            Cantidad_del_Producto = int(input())
            print()

            if Cantidad_del_Producto > 0:
                break

            else:
                print("ERROR! La Cantidad del producto no puede ser menor o igual a 0")

        except ValueError:
            print("ERROR! Por favor ingrese solo números")
            print()

    Subtotal_del_Producto = Precio_Unitario_del_Producto * Cantidad_del_Producto
    Subtotal += Subtotal_del_Producto
    IVA = 0.19
    Impuesto_Total = Subtotal * IVA
    
print(f"{NEGRITA}-"*65)
print(f"{RESET}¿Tiene membresia VIP? Escriba el codigo sino de ENTER")
Es_VIP = input()

Codigo = "1234"

if Es_VIP == Codigo:
    Descuento = Subtotal * 0.10
    Total = Subtotal - Descuento + Impuesto_Total
    
else:
    Descuento = 0

    Total = Subtotal - Descuento + Impuesto_Total

print(f"{NEGRITA}={RESET}"*65)
print("Registro de la venta".center(65))
print(f"{NEGRITA}={RESET}"*65)
print(f"Nombre del cliente: {Nombre_del_cliente}")
print(f"{NEGRITA}-{RESET}"*65)
print(f"Cantidad de productos: {Cantidad_de_Productos}")
print(f"{NEGRITA}-{RESET}"*65)
print(f"Subtotal de la compra: $ {Subtotal}")
print(f"{NEGRITA}-{RESET}"*65)
print(f"IVA: $ {Impuesto_Total}")
print(f"{NEGRITA}-{RESET}"*65)
print(f"Descuento aplicado del 10% por ser VIP: $ {Descuento}")
print(f"{NEGRITA}={RESET}"*65)
print(f"Total a pagar: $ {Total}")
print(f"{NEGRITA}={RESET}"*65)