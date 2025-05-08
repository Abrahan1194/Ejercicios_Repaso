inventario = {}

def agregar_producto(inventario_local):
    print("\033[94m\033[1mAñadir Producto\033[0m")
    nombre = input("\033[1mIngrese el nombre del producto: ").strip()
    if nombre in inventario_local:
        print(f"\033[93m El producto '{nombre}' ya existe\033[0m")
        return

    while True:
        try:
            precio_str = input("\033[1mIngrese el precio del producto: ").replace(',', '.')
            precio = float(precio_str)
            if precio < 0:
                print("\033[93m El precio debe ser un valor positivo.\033[0m")
                continue
            break
        except ValueError:
            print("\033[93m Por favor, ingrese un numero valido para el precio.\033[0m")

    while True:
        try:
            cantidad_str = input("\033[1mIngrese la cantidad disponible: ")
            cantidad = int(cantidad_str)
            if cantidad < 0:
                print("\033[93m La cantidad debe ser un valor positivo.\033[0m")
                continue
            break
        except ValueError:
            print("\033[93m Por favor, ingrese un numero entero valido para la cantidad.\033[0m")

    inventario_local[nombre] = (precio, cantidad)
    print(f"\033[1mEl producto '{nombre}' ha sido añadido al inventario.\033[0m")

def consultar_producto(inventario_local):
    print("\n\033[94m\033[1mConsultar Producto\033[0m")
    nombre = input("\033[1mIngrese el nombre del producto que desea consultar: ").strip()
    if nombre in inventario_local:
        precio, cantidad = inventario_local[nombre]
        print("\033[1m" + "-" * 30 + "\033[0m")
        print(f"\033[1m| {'Producto':<15} | {nombre:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")
        print(f"\033[1m| {'Precio':<15} | ${precio:11,.2f} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")
        print(f"\033[1m| {'Cantidad':<15} | {cantidad:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")
    else:
        print(f"\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")

def actualizar_precio(inventario_local):
    print("\n\033[94m\033[1mActualizar Precio\033[0m")
    nombre = input("\033[1mIngrese el nombre del producto cuyo precio desea actualizar: ").strip()
    if nombre in inventario_local:
        while True:
            try:
                nuevo_precio_str = input("\033[1mIngrese el nuevo precio: ").replace(',', '.')
                nuevo_precio = float(nuevo_precio_str)
                if nuevo_precio < 0:
                    print("\033[93mEl precio debe ser un valor positivo.\033[0m")
                    continue
                inventario_local[nombre] = (nuevo_precio, inventario_local[nombre][1])
                print(f"\033[1mEl precio de '{nombre}' ha sido actualizado a ${nuevo_precio:,.2f}.\033[0m")
                break
            except ValueError:
                print("\033[93mPor favor, ingrese un numero valido para el precio.\033[0m")
    else:
        print(f"\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")

def eliminar_producto(inventario_local):
    print("\n\033[94m\033[1mEliminar Producto\033[0m")
    nombre = input("\033[1mIngrese el nombre del producto que quiere eliminar: ").strip()
    if nombre in inventario_local:
        del inventario_local[nombre]
        print(f"\033[1mEl producto '{nombre}' ha sido eliminado.\033[0m")
    else:
        print(f"\033[93m El producto no se encuentra en el inventario.\033[0m")

def calcular_valor_total(inventario_local):
    print("\n\033[94m\033[1mValor Total del Inventario\033[0m")
    valor_total_lambda = lambda inventario: sum(precio * cantidad for precio, cantidad in inventario.values())
    valor_total = valor_total_lambda(inventario_local)
    print(f"\033[1mEl valor total del inventario es: ${valor_total:,.2f}\033[0m")
    return valor_total

def mostrar_inventario(inventario_local):
    print("\n\033[94m\033[1mMostrar Inventario\033[0m")
    if not inventario_local:
        print("\033[1mEl inventario está vacío.\033[0m")
        return
    print("\033[1m   Inventario Actual   \033[0m")
    for nombre, (precio, cantidad) in inventario_local.items():
        print(f"\033[1mProducto: {nombre}, Precio: ${precio:,.2f}, Cantidad: {cantidad}\033[0m")
    print("-" * 35)




while True:
    print("\n\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[94m\033[1m" + "  SISTEMA DE INVENTARIO  ".center(35) + "\033[0m")
    print("\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[1m  Opciones:\033[0m")
    print(f"\033[1m  1. Añadir producto{''.ljust(31)}\033[0m")
    print(f"\033[1m  2. Consultar producto{''.ljust(29)}\033[0m")
    print(f"\033[1m  3. Actualizar precio{''.ljust(30)}\033[0m")
    print(f"\033[1m  4. Eliminar producto{''.ljust(30)}\033[0m")
    print(f"\033[1m  5. Calcular valor total{''.ljust(24)}\033[0m")
    print(f"\033[1m  6. Mostrar inventario{''.ljust(27)}\033[0m")
    print(f"\033[1m  7. Salir{''.ljust(34)}\033[0m")
    print("\033[94m" + "═" * 35 + "\033[0m")

    opcion = input("\033[94m\033[1mSeleccione una opción: \033[0m")

    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        consultar_producto(inventario)
    elif opcion == '3':
        actualizar_precio(inventario)
    elif opcion == '4':
        eliminar_producto(inventario)
    elif opcion == '5':
        valor_total = calcular_valor_total(inventario)
    elif opcion == '6':
        mostrar_inventario(inventario)
    elif opcion == '7':
        print("\n\033[94m\033[1mSaliendo del programa\033[0m")
        break
    else:
        print("\n\033[93m Opción inválida. Por favor, seleccione una opción válida.\033[0m")