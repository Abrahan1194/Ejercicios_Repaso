Biblioteca = []
id = int(0)
print("\n--- Menú de biblioteca ---")
print("1. Crear libro ")
print("2. Consultar libros")
print("3. Modificar libro")
print("4. Eliminar libro")
print("5. Salir")

opcion = input("Seleccione una opción: ")

while True:
          if opcion == '1':
            
            id =+1
            titulo = input("Ingrese el titulo del lirbo: ")
            autor = input("Ingrese Autor: ")
            año= int(input("Ingrese correo del usuario: "))
            libro = {"ID": id,"Titulo": titulo, "Autor": autor, "Año pubñicacion": año}
            Biblioteca.append(libro)
            print("libro creado correctamente.")

            print(Biblioteca)