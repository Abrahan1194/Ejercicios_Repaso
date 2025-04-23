usuarios = []

while True:
    print("\n--- Menú de Usuarios ---")
    print("1. Crear usuario")
    print("2. Consultar usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        correo= input("Ingrese correo del usuario: ")
        usuario = {"nombre": nombre, "edad": edad, "correo": correo}
        usuarios.append(usuario)
        print("Usuario creado correctamente.")

    elif opcion == '2':
        if usuarios:
            print("\n--- Lista de Usuarios ---")
            for i, usuario in enumerate(usuarios):
                print(f"{i+1}. {usuario['nombre']}, {usuario['edad']} años, {usuario['correo']}")
        else:
            print("No hay usuarios registrados.")

    elif opcion == '3':
        if usuarios:
            usuario_a_modificar = int(input("Ingrese el número del usuario a modificar: ")) - 1
            if 0 <= usuario_a_modificar < len(usuarios):
                nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ")
                if nombre:
                    usuarios[usuario_a_modificar]["nombre"] = nombre
                edad = input("Ingrese la nueva edad (o presione Enter para mantener la actual): ")
                if edad:
                    usuarios[usuario_a_modificar]["edad"] = int(edad)
                correo = input("Ingrese la nueva ciudad (o presione Enter para mantener la actual): ")
                if correo:
                    usuarios[usuario_a_modificar]["correo"] = correo
                print("Usuario modificado correctamente.")
            else:
                print("Número de usuario inválido.")
        else:
            print("No hay usuarios registrados.")

    elif opcion == '4':
        if usuarios:
            usuario_a_eliminar = int(input("Ingrese el número del usuario a eliminar: ")) - 1
            if 0 <= usuario_a_eliminar < len(usuarios):
                del usuarios[usuario_a_eliminar]
                print("Usuario eliminado correctamente.")
            else:
                print("Número de usuario inválido.")
        else:
            print("No hay usuarios registrados.")

    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")