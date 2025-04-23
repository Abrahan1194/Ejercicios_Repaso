lista_personas =[]

print("\n Ingrese el numero de la accion que desea realizar" \
"\n1 Crear Usuario" \
"\n2 consultar Usuarios" \
"\n3 EliminarUsuario" \
"\n4 Modoficar usuario")
print("\n========================================================")
opciones = int(input(""))
if opciones == '1':
     nombre=input("\nIngrese Nombre: ")
     lista_personas.append([nombre])
     apellido=input("\nIngrese apellido: ")
     lista_personas.append([apellido])
     correo=input("\nIngrese correo: ")
     lista_personas.append([correo])
     edad = int(input("\nIngrese edad: "))
     lista_personas.append([edad])
     usuario={"nombre":nombre ,"Apellido": apellido,"correo":correo, "edad":edad}
     lista_personas.append(usuario)
     print("Usuario creado correctamente")


elif opciones == '2':
     print("\nLa lista de usarios es :")
     for i ,in enumerate(lista_personas):
          print(f"{i+1}.{lista_personas['nombre']},{lista_personas['apellido']},{lista_personas['correo']},{lista_personas['edad']}")
     else:
          print("No hay registrados")

elif opciones =='3':
     usuario_a_actualizar=int(input("Ingrese el numero usuario que desee borrar:  "))