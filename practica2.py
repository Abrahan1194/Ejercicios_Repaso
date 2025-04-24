productos = []

while True:
    nom_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nom_producto.lower() == 'fin':
        break

    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario < 0:
                print("Digite un valor válido")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido")

    while True:
        try:
            cantidad_productos = int(input("Ingrese la cantidad de productos: "))
            if cantidad_productos <= 0:
                print("Ingrese un valor válido")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido")

    while True:
        try:
            porcet_descuento = float(input("Ingrese el descuento (%): "))
            if not 0 <= porcet_descuento <= 100:
                print("Descuento inválido")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido")

    sub_total = precio_unitario * cantidad_productos
    descuento = (sub_total * porcet_descuento) / 100
    total = sub_total - descuento

    productos.append({
        "nombre": nom_producto,
        "precio_unitario": precio_unitario,
        "cantidad": cantidad_productos,
        "descuento": porcet_descuento,
        "subtotal": sub_total,
        "total": total
    })

print("\nResumen de la compra:")
total_general = 0
for p in productos:
    print(f"Producto: {p['nombre']}")
    print(f"  Precio unitario: {p['precio_unitario']:.2f}")
    print(f"  Cantidad: {p['cantidad']}")
    print(f"  Subtotal: {p['subtotal']:.2f}")
    print(f"  Descuento: {p['descuento']}%")
    print(f"  Total con descuento: {p['total']:.2f}\n")
    total_general += p['total']

print(f"Total general a pagar: {total_general:.2f}")