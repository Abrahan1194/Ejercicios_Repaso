Biblioteca = {}
id = 0


while True:
          print("\n--- Menú de biblioteca ---")
          print("1. Crear libro ")
          print("2. Consultar libros")
          print("3. Modificar libro")
          print("4. Eliminar libro")
          print("5. Salir")

          opcion = input("Seleccione una opción: ")

          if opcion == '1':
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese Autor: ")
            año= int(input("Ingrese año de lazamiento: "))
            id = id +1
            Biblioteca[id] = {
                     "Titulo": titulo, 
                     "Autor": autor, 
                     "Año publicacion": año}
            print("libro creado correctamente.")

          elif opcion  == '2':
               for i in range(len(titulo)):
                print("\nLa lista libros es :")
                print(Biblioteca)
                i = i+1
          else:
                print("No hay registrados")


          if opcion == '3':
               if Biblioteca:
                  libro_a_eliminar=(input("Ingrese el ID del usuario a eliminar:"))-1
                  if 0 <= libro_a_eliminar < len(id):
               
          
          
                
            
