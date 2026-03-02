print("=== SISTEMA DE VENTAS ===")

nombre_cliente = input("Nombre del cliente: ")
vip = input("¿El cliente es VIP? (si/no): ").lower()

subtotal = 0
total_productos = 0

while True:
    print("\n--- Agregar Producto ---")
    nombre_producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario: "))
    
    total_producto = cantidad * precio
    subtotal += total_producto
    total_productos += cantidad
    
    print(f"Total del producto {nombre_producto}: ${total_producto:.2f}")
    
    continuar = input("¿Desea agregar otro producto? (si/no): ").lower()
    if continuar == "no":
        break

# Descuento VIP (10%)
descuento = 0
if vip == "si":
    descuento = subtotal * 0.10

subtotal_con_descuento = subtotal - descuento

# IVA 19%
iva = subtotal_con_descuento * 0.19

total_pagar = subtotal_con_descuento + iva

# FACTURA
print("\n========== FACTURA ==========")
print(f"Cliente: {nombre_cliente}")
print(f"Productos comprados: {total_productos}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento VIP: -${descuento:.2f}")
print(f"Subtotal con descuento: ${subtotal_con_descuento:.2f}")
print(f"IVA (19%): ${iva:.2f}")
print(f"TOTAL A PAGAR: ${total_pagar:.2f}")
print("Gracias por su compra")


