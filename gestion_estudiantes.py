list_student = {
  1: {"nombre": "Juan Perez", "nota": 3.5, "edad": 20},
  2: {"nombre": "Maria Gomez", "nota": 4.2, "edad": 19},
  3: {"nombre": "Pedro Ramirez", "nota": 2.1, "edad": 21},
  4: {"nombre": "Ana Hurtado", "nota": 4.8, "edad": 18},
  5: {"nombre": "Carlos Piedrahita", "nota": 1.9, "edad": 20}

}
def option_1():
        
        name_complete = input("\n\033[1m\033[36mIngrese Nombre Estudiante: \033[0m")  
        age = input("\033[1m\033[36mIngrese la edad del estudiante: \033[0m")  
        note = (input("\033[1m\033[36mIngrese notas del estudiante separada por espacios: \033[0m")).split()
    
        student = {
                    "nombre": name_complete,
                    "edad": age,
                    "nota": note,
                }
        list_student[count_Id] = student
        print(f"\n\033[1m\033[32mEstudiante agregado con ID {count_Id}\033[0m")  

def option_2():
        if not list_student:
         print("\033[1m\033[31mNo hay estudiantes registrados.\033[0m")
         return

        id_search = input("\033[1mIngrese el ID del estudiante que desea buscar:\033[0m ")
        try:
            count_Id = int(id_search) 
            if count_Id in list_student:
                student = list_student[count_Id]
                print(f"\n\033[1m\033[36mDetalles del estudiante con ID:\033[0m \033[1m\033[33m{count_Id}\033[0m")
                print(f"\033[1m\033[34mNombre Completo:\033[0m {student['nombre']}")
                print(f"\033[1m\033[34mEdad:\033[0m {student['edad']}")
                print(f"\033[1m\033[34mNota:\033[0m {student['nota']}")
            else:
                print(f"\033[1m\033[31mNo se encontró ningún estudiante con el ID:\033[0m \033[1m\033[33m{count_Id}\033[0m")
        except ValueError:
            print("\033[1m\033[31mError: El ID debe ser un número entero.\033[0m")


def option_3():
      
      if list_student:
            try:
                id_eliminate = int(input("\033[1m\033[36mIngrese el ID del Estudiante a eliminar: \033[0m"))  
                if id_eliminate in list_student:
                    del list_student[id_eliminate]
                    print("\033[1m\033[32mEstudiante eliminado correctamente\033[0m") 
                else:
                    print("\033[1m\033[31mID no encontrado\033[0m")  
            except ValueError:
                print("\033[1m\033[31mID inválido\033[0m")  
      else:
            print("\033[1m\033[31mNo hay estudiantes\033[0m")  

def option_4():
       
       if list_student:
            try:
                id_modify = int(input("\033[1m\033[36mIngrese el ID del estudiante que desea modificar: \033[0m"))  
                if id_modify in list_student:
                    student = list_student[id_modify]

                    new_age = input("\033[1m\033[36mIngrese nueva edad (Enter para mantener): \033[0m")  
                    if new_age:
                        student["edad"] = new_age

                    new_note = input("\033[1m\033[36mIngrese nueva nota (Enter para mantener): \033[0m")  
                    if new_note:
                        student["nota"] = new_note
                        note = new_note
                    print("\033[1m\033[92mEstudiante modificado correctamente\033[0m")  
                    
                else:
                    print("\033[1m\033[31mID ingresado incorrecto\033[0m")  
            except ValueError:
                print("\033[1m\033[31mID invalido\033[0m") 
       else:
            print("\033[1m\033[31mNo hay estudiantes para modificar\033[0m")  


def option_7():
      print("\n\033[1m\033[35mSaliendo del programa\033[0m")  
      exit()


count_Id = 6
while True:
            print("\n")
            print("\033[1m\033[34m=\033[0m" * 30) 
            print("\033[1m\033[34m=\033[0m" * 30)  
            options = (input("\033[1m\033[32mGestion de estudiantes :\033[0m"  
                                "\n\033[1m\033[33m1\033[0m Agregar estudiante."
                                "\n\033[1m\033[33m2\033[0m Buscar estudiante .(por ID)"
                                "\n\033[1m\033[33m3\033[0m Eliminar estudiante. "
                                "\n\033[1m\033[33m4\033[0m Actualizar información de un estudiante."
                                "\n\033[1m\033[33m5\033[0m Calcular el promedio de notas:"
                                "\n\033[1m\033[33m6\033[0m Lista de estudiantes con notas inferiores  3.0"
                                "\n\033[1m\033[33m7\033[0m Salir."
                                "\n\033[1m\033[35mOpción = \033[0m")) 
            
            if options == '1':
                option_1()
                count_Id = count_Id + 1
                
            elif options =='2':
                option_2()
                
            elif options =='3':
                option_3()
                
            elif options =='4':
                option_4()
                
            elif options =='7':
                option_7()
                