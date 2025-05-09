inventario = {}  # Aquí guardamos los productos y su información

def agregar_producto(inventario_local):
    nombre = input("Ingrese el nombre del producto: ").strip()  # Pide el nombre del producto
    if nombre in inventario_local:  # Revisa si el producto ya existe
        print(f"El producto '{nombre}' ya existe en el inventario.")
        return  # Sale de la función si el producto ya existe

    while True:  # Repite hasta que se ingrese un precio válido
        try:
            precio_str = input("Ingrese el precio del producto: ").replace(',', '.')  # Pide el precio
            precio = float(precio_str)  # Convierte el precio a número
            if precio < 0:
                print("El precio debe ser un valor positivo.")
                continue  # Vuelve a pedir el precio si es negativo
            break  # Sale del bucle si el precio es válido
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    while True:  # Repite hasta que se ingrese una cantidad válida
        try:
            cantidad_str = input("Ingrese la cantidad disponible: ")  # Pide la cantidad
            cantidad = int(cantidad_str)  # Convierte la cantidad a número entero
            if cantidad < 0:
                print("La cantidad debe ser un valor positivo.")
                continue  # Vuelve a pedir la cantidad si es negativa
            break  # Sale del bucle si la cantidad es válida
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")

    inventario_local[nombre] = (precio, cantidad)  # Guarda el nombre, precio y cantidad en el inventario
    print(f"El producto '{nombre}' ha sido añadido al inventario.")

def consultar_producto(inventario_local):
    nombre = input("Ingrese el nombre del producto que desea consultar: ").strip()  # Pide el nombre del producto a buscar
    if nombre in inventario_local:  # Revisa si el producto está en el inventario
        precio, cantidad = inventario_local[nombre]  # Obtiene el precio y la cantidad del producto
        print(f"Producto: {nombre}")
        print(f"Precio: ${precio:,.2f} COP")
        print(f"Cantidad disponible: {cantidad}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

def actualizar_precio(inventario_local):
    nombre = input("Ingrese el nombre del producto cuyo precio desea actualizar: ").strip()  # Pide el nombre del producto a actualizar
    if nombre in inventario_local:  # Revisa si el producto está en el inventario
        while True:  # Repite hasta que se ingrese un precio válido
            try:
                nuevo_precio_str = input("Ingrese el nuevo precio: ").replace(',', '.')  # Pide el nuevo precio
                nuevo_precio = float(nuevo_precio_str)  # Convierte el nuevo precio a número
                if nuevo_precio < 0:
                    print("El precio debe ser un valor positivo.")
                    continue  # Vuelve a pedir el precio si es negativo
                inventario_local[nombre] = (nuevo_precio, inventario_local[nombre][1])  # Actualiza el precio del producto
                print(f"El precio de '{nombre}' ha sido actualizado a ${nuevo_precio:,.2f} COP.")
                break  # Sale del bucle si el precio es válido
            except ValueError:
                print("Por favor, ingrese un número válido para el precio.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

def eliminar_producto(inventario_local):
    nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()  # Pide el nombre del producto a eliminar
    if nombre in inventario_local:  # Revisa si el producto está en el inventario
        del inventario_local[nombre]  # Elimina el producto del inventario
        print(f"El producto '{nombre}' ha sido eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

def calcular_valor_total(inventario_local):
    valor_total_lambda = lambda inventario: sum(precio * cantidad for precio, cantidad in inventario.values())  # Función para calcular el valor total
    valor_total = valor_total_lambda(inventario_local)  # Calcula el valor total del inventario
    return valor_total

def mostrar_inventario(inventario_local):
    if not inventario_local:  # Revisa si el inventario está vacío
        print("El inventario está vacío.")
        return
    print("\n--- Inventario Actual ---")
    for nombre, (precio, cantidad) in inventario_local.items():  # Recorre cada producto en el inventario
        print(f"Producto: {nombre}, Precio: ${precio:,.2f} COP, Cantidad: {cantidad}")  # Muestra la información del producto
    print("-\n"*50)

print("\nInventario")  # Título del programa
while True:  # Bucle principal del programa
    print("\n1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")  # Pide al usuario que elija una opción

    if opcion == '1':
        agregar_producto(inventario)  # Llama a la función para agregar un producto
    elif opcion == '2':
        consultar_producto(inventario)  # Llama a la función para consultar un producto
    elif opcion == '3':
        actualizar_precio(inventario)  # Llama a la función para actualizar el precio de un producto
    elif opcion == '4':
        eliminar_producto(inventario)  # Llama a la función para eliminar un producto
    elif opcion == '5':
        valor_total = calcular_valor_total(inventario)  # Calcula el valor total del inventario
        print(f"El valor total del inventario es: ${valor_total:,.2f} COP")
    elif opcion == '6':
        mostrar_inventario(inventario)  # Llama a la función para mostrar el inventario
    elif opcion == '7':
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Sale del bucle principal y termina el programa
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
