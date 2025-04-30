agenda = {}
id_persona = 1

while True :
    print("\n")  
    print("\033[1m\033[35m=" *30)
    print("\033[1m\033[35m=" *30)

    opciones = int(input("\n\033[1m\033[36mAgenda De contactos\033[0m"
                            "\n\033[1m\033[36m1. \033[0mAgregar Contactos "
                            "\n\033[1m\033[36m2. \033[0mConsultar agenda "
                            "\n\033[1m\033[36m3. \033[0mActualizar Agenda "
                            "\n\033[1m\033[36m4. \033[0mEliminar Contacto "
                            "\n\033[1m\033[36m5. \033[0mSalir "
                            "\n\033[1m\033[36mOpcion : \033[0m"))
     
    if opciones == 1:
          nombre = (input("\n\033[1m\033[36mAgregue Nombre contacto :  \033[0m"))
          telefono = (input("\033[1m\033[36mAgregue Telefono del Contacto :  \033[0m"))
          email = (input("\033[1m\033[36mAgregue el Email :  \033[0m"))

          datos = {
           "nombre" : nombre,
           "telefono" : telefono,
           "email" : email, 
               }
          agenda [id_persona] = datos
          id_persona += 1
          print(input("\033[1m\033[33mContacto Agregado!"))
    elif opciones == 2 :
        if agenda :
          print(f"\n\033[1m\033[36m{'ID':<15} {'nombre':<20} {'telefono':<20} {'email':<20}\033[0m")
          print("\033[34m" + "-" * 70 + "\033[0m")
            
          for id in agenda:
              datos = agenda[id]
              print(
                    f"\033[1m\033[32m{id:<15}\033[0m"
                    f"\033[1m{datos['nombre']:<24}"
                    f"\033[1m{datos['telefono']:<24}"
                    f"\033[1m{datos['email']:<24}"
               )
     
            
          
           

 
     


