productos = []

while True:
    nombre_producto = input("Ingrese el nombre del producto o exit para finalizar la compra: ")
    if nombre_producto.lower() == "exit" :
        break

    while True:
        try :
            precio_unitario = float(input("Ingrese precio Unitario del producto :"))
            if precio_unitario < 0:
                print("Valor Ingresado Invalido")
            else:
                break
        except ValueError :
            print ("Ingrese Un valor Valido")

    while True: 
        try :
            cantidad_productos =int(input("Ingrese Cantidad de productos :"))
            if cantidad_productos <= 0 :
                print("Valor Ingresado Incorrecto")
            else:
                break
        except ValueError :
              print ("Ingrese Un valor Valido")
    
    while True:
        try :
            porcentaje_descuento = float(input("Ingrese porcentaje de descuento entre 0 y 100 %: "))
            if not 0 <= porcentaje_descuento <=100 :
              print("Descuento Invalido")
            else :
                break
        except ValueError :
            print("Ingrese Descuento Dentro del rango")
                  
    Sub_total = precio_unitario * cantidad_productos
    descuento =  ( Sub_total * porcentaje_descuento)  /100
    total_compra = Sub_total - descuento    


    productos.append({
        "nombre": nombre_producto,
        "Valor producto": precio_unitario,
        "Cantidad": cantidad_productos,
        "Descuento" : porcentaje_descuento,
        "Sub Total" :Sub_total,
        "Total" : total_compra,
        })   
    
    
    print("\nResumen De La compra")
    total_compra_general = 0 
    for i in productos :
        print(f"Nombre producto: {i['nombre']}")
        print(f"Precio producto es :{i['Valor producto']:.2f}")
        print(f"Cantidad : {i['Cantidad']:.2f}")
        print(f"Descuento es :{i['Descuento']:.2f}")
        print(f"Sub Total: {i['Sub Total']:.2f}")
        total_compra_general += i['Total']


print(f"Valor total de la compra es:{total_compra_general :.2f}")
   
    

