# Listas vacías para almacenar los datos ingresados de cada producto
nombre_producto = []
precio_unitario = []
cantidad_producto = []
porcentaje_descuento = []
valor_descuento = []
sub_total = []
totales = []
# Bucle principal para ingresar productos
while True :
    nombre= input("\nIngrese el Nombre del Producto o exit para salir :")
    if nombre.lower() == "exit" : # Se rompe el ciclo si el usuario escribe "exit" ,el .lower por si ingresa mayuscula o miniscula
        break
    # Bucle para validar el precio del producto ,No se aceptan valores negativos 
    while True :
        try :
            precio = float(input("\nIngrese valor del producto: "))
            if precio < 0 :
                print("Valor ingresado incorrecto")
            else:
                break
        except ValueError :
               print("Ingrese un valor correcto")
    # Bucle para validar la cantidad del producto ,No se aceptan valores negativos 
    while True:
        try:
            cantidad = int(input("\nIngrese Cantidad del producto:"))
            if cantidad <= 0 :
                print("Numero Ingresado Invalido")
            else:
                break
        except ValueError :
               print("Ingrese valor correcto")
        # Bucle para validar el porcentaje de descuento ,El descuento debe estar entre 0% y 100%
    while True :
        try :
            porcentaje = float(input("\nIngrese el descuento del producto :"))
            if not 0 <= porcentaje <= 100 :
                print("valor Ingresado Invalido") 
            else:
                break
        except ValueError :
                print("Ingrese Valor correcto: ")


    # Calculos
    sub_totals= precio * cantidad
    Descuento = (sub_totals * porcentaje)/100
    compra_total = sub_totals-Descuento
    # Se almacenan los datos en sus respectivas listas
    nombre_producto.append(nombre)
    precio_unitario.append(precio)
    cantidad_producto.append(cantidad)
    porcentaje_descuento.append(porcentaje)
    sub_total.append(sub_totals)
    totales.append(compra_total)
    valor_descuento.append(Descuento)
#  Encabezado resumen compra 
print("="*60)
print("\nResumen De La compra")
print("="*60)

compra_total_general = 0
# Recorrido de los productos ingresados para mostrar su resumen
#Se está asumiendo que todas las listas ,tienen la misma cantidad de datos 
#range hace que el ciclo for se recorre la cantidad de indices que tenga la lista
# el :.2f para que imprima dos decimales
for i in range(len(nombre_producto)):
     print("="*60)
     print(f"\nItem:                  {"":<20}Valor:{"":<20}")
     print(f"\nNombre del producto   :{"":<20}{nombre_producto[i]}")
     print(f"\nPrecio del producto   :{"":<20}{precio_unitario[i]:.2f}")
     print(f"\nCantidad de producto  :{"":<20}{cantidad_producto[i]:.2f}")
     print(f"\nPorcentaje Descuento  :{"":<20}{porcentaje_descuento[i]:.2f}")
     print(f"\nValor Descuento       :{"":<20}{valor_descuento[i]:.2f}")
     print(f"\nSub total de la compra:{"":<20}{sub_total[i]:.2f}")
     print("="*60)
     compra_total_general += totales[i]  # Sumar el total del producto al total general
# Mostrar el total acumulado 
     
print(f"\ncompra total es :{compra_total_general:.2f}")

