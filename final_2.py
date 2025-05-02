# --- Menú del Programa de Gestión de Calificaciones ---
print("\n--- Menú del Programa de Gestión de Calificaciones ---")
print("Este programa te permite realizar las siguientes acciones:")
print("1. Determinar el estado de aprobación de una calificación.")
print("2. Calcular el promedio de una lista de calificaciones.")
print("3. Contar cuántas calificaciones son mayores que un valor específico.")
print("4. Verificar si una calificación específica está en la lista y cuántas veces aparece.")
print("5. Salir del programa.")
print("------------------------------------------------------")

lista_de_calificaciones = [] # Inicializamos la lista aquí

while True:
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == '1':
        # --- Determinar estado de aprobación ---
        print("\n--- Determinar estado de aprobación ---")
        while True:
            calificacion_str = input("Ingresa una calificación numérica (0-100): ")
            try:
                calificacion = int(calificacion_str)
                if 0 <= calificacion <= 100:
                    break
                else:
                    print("Por favor, ingresa una calificación entre 0 y 100.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        if calificacion >= 60:
            print("¡Aprobado!")
        else:
            print("Reprobado.")

    elif opcion == '2':
        # --- Calcular el promedio ---
        print("\n--- Calcular el promedio ---")
        while True:
            calificaciones_str = input("Ingresa una lista de calificaciones separadas por comas: ")
            lista_calificaciones_str = calificaciones_str.split(',')
            lista_calificaciones_temp = []
            valida = True
            for calif_str in lista_calificaciones_str:
                try:
                    calif = int(calif_str.strip())
                    if 0 <= calif <= 100:
                        lista_calificaciones_temp.append(calif)
                    else:
                        print("Una de las calificaciones ingresadas no está entre 0 y 100. Intenta de nuevo.")
                        valida = False
                        break
                except ValueError:
                    print("Entrada inválida en la lista de calificaciones. Por favor, ingresa números separados por comas.")
                    valida = False
                    break
            if valida and lista_calificaciones_temp:
                lista_de_calificaciones = lista_calificaciones_temp # Actualizamos la lista principal
                suma_calificaciones = 0
                for calif in lista_de_calificaciones:
                    suma_calificaciones += calif
                promedio = suma_calificaciones / len(lista_de_calificaciones)
                print(f"El promedio de las calificaciones es: {promedio:.2f}")
                break
            elif valida and not lista_calificaciones_temp:
                print("No ingresaste ninguna calificación. Intenta de nuevo.")

    elif opcion == '3':
        # --- Contar calificaciones mayores ---
        print("\n--- Contar calificaciones mayores ---")
        if not lista_de_calificaciones:
            print("Primero debes ingresar una lista de calificaciones (opción 2).")
        else:
            while True:
                valor_comparacion_str = input("Ingresa un valor para comparar las calificaciones: ")
                try:
                    valor_comparacion = int(valor_comparacion_str)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")

            contador_mayores = 0
            indice = 0
            while indice < len(lista_de_calificaciones):
                if lista_de_calificaciones[indice] > valor_comparacion:
                    contador_mayores += 1
                indice += 1
            print(f"Hay {contador_mayores} calificaciones mayores que {valor_comparacion}.")

    elif opcion == '4':
        # --- Verificar y contar calificaciones específicas ---
        print("\n--- Verificar y contar calificaciones específicas ---")
        if not lista_de_calificaciones:
            print("Primero debes ingresar una lista de calificaciones (opción 2).")
        else:
            while True:
                calificacion_especifica_str = input("Ingresa una calificación específica para verificar y contar: ")
                try:
                    calificacion_especifica = int(calificacion_especifica_str)
                    if 0 <= calificacion_especifica <= 100:
                        break
                    else:
                        print("Por favor, ingresa una calificación entre 0 y 100.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")

            contador_especifica = 0
            encontrada = False
            for calif in lista_de_calificaciones:
                if calif == calificacion_especifica:
                    contador_especifica += 1
                    encontrada = True
                    continue
                elif calif > calificacion_especifica + 10:
                    break 
            if encontrada:
                print(f"La calificación {calificacion_especifica} aparece {contador_especifica} veces en la lista.")
            else:
                print(f"La calificación {calificacion_especifica} no se encontró en la lista.")

    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción del menú (1-5).")