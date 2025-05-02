#Creacion de Menu
print("-"*50)
print("\n Menu Programa Gestion de Datos:")
print("\n Escoge una accion a realizar :")
print("1. Determinar estado de aprobacion.")
print("2. Calcular promedio de notas ingresadas.")
print("3. Contar cuantas calificaciones son mayores a un valor especifico Ingresado.")
print("4. Contar cuantas veces se repite una calificacion es espesifica ingresada por el usuario.")
print("5. Salir")   
print("-"*50)


calificaciones = []

while  True:
    opcion = input("\nIngrese una opcion del 1 al 5 : ")
    while True:
        if opcion == '1' :
            nota_final_letras = input("Ingrese calificacion del estudiante para determinar si aprobo o no aprobo:")#se ingresa en str despues se convierte
            try :
                nota_final =int(nota_final_letras)
                if 0 <= nota_final<=100:
                    break
                else:
                    print("Ingrese una calificacion valida entre 0 y 100:")
            
            except ValueError :
                print("Valor Invalido ingrese una calificacion :")
    if nota_final >= 60 :
         print("\nAprobado")

    else :
         print("\nReprobado")
