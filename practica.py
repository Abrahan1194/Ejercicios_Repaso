lista_personas =[]
while True:
 print("\n Ingrese el numero de la accion que desea realizar" \
"\n1 Crear Usuario" \
"\n2 consultar Usuarios" \
"\n3 Eliminar Usuario" \
"\n4 Modoficar usuario" \
"\n5 Salir")

 print("\n========================================================")
 opciones = int(input(""))
 if opciones == 1:
     nombre=input("\nIngrese Nombre: ")
     apellido=input("\nIngrese apellido: ")
     correo=input("\nIngrese correo: ")
     edad = int(input("\nIngrese edad: "))
     usuario = {"nombre": nombre ,"Apellido": apellido,"correo": correo,"edad": edad}
     lista_personas.append(usuario) 
     print("Usuario creado correctamente")

 elif opciones == 2:
     if lista_personas:
      print("\nLa lista de usarios es :")
      for i ,usuario in enumerate(lista_personas):
          print(f"{i+1}. {usuario['nombre']}, {usuario['Apellido']}, {usuario['correo']}, {usuario['edad']}")
     else:
          print("No hay registrados")

 elif opciones == 4:
     if lista_personas:
        usuario_a_actualizar=int(input("Ingrese el numero usuario que desee modoficar:  "))-1
        if 0 <= usuario_a_actualizar < len(lista_personas):
            nombre =input("Ingrese nuevo nombre, o presione enter para mentener el nombre: ")
            if nombre:
                lista_personas [usuario_a_actualizar]["nombre"]= nombre
                apellido =input("Ingrese nuevo apellido, o presione enter para mentener el apellido: ")
            if apellido:
                 lista_personas [usuario_a_actualizar]["Apellido"]= apellido
                 edad =input("Ingrese nueva edad, o presione enter para matener la edad: ") 
            if edad:
                 lista_personas [usuario_a_actualizar]["edad"]= edad

                 correo =input("Ingrese nuevo correo, o presione enter para mentener el correo: ")
            if correo:
                 lista_personas [usuario_a_actualizar]["correo"]= correo
                 print("Usuario modificado")
            else:
                print("Numero ingresado incorrecto")
        else:
                print("No hay usuarios para modificar")
 elif opciones == 3:
     if lista_personas:
        usuario_a_eliminar=int(input("Ingrese el numero del usuario a eliminar: 1"))-1
        if 0 <= usuario_a_eliminar < len(lista_personas):
          del lista_personas[usuario_a_eliminar]
          print("usuario eliminado correctamente !")
        else:
          print("numero de usuario incorrecto")
     else:
          print("No hay usuarios")

 elif opciones == 5:
     print ("Saliendo el programa :")
     break
 else:
     print("opcion Invalida")