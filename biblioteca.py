lista_libros = {}
contador_id = 1

while True:
    print("\n")
    print("\033[1m\033[34m=\033[0m" * 30) 
    print("\033[1m\033[34m=\033[0m" * 30)  
    opciones = int(input("\033[1m\033[32mMenú de Libros\033[0m"  
                         "\n\033[1m\033[33m1\033[0m Agregar Libro"
                         "\n\033[1m\033[33m2\033[0m Consultar Libros"
                         "\n\033[1m\033[33m3\033[0m Eliminar Libro"
                         "\n\033[1m\033[33m4\033[0m Modificar Libro"
                         "\n\033[1m\033[33m5\033[0m Salir"
                         "\n\033[1m\033[35mOpción = \033[0m"))  

    if opciones == 1:
        titulo = input("\n\033[1m\033[36mIngrese Título: \033[0m")  
        autor = input("\033[1m\033[36mIngrese Autor: \033[0m")  
        año = (input("\033[1m\033[36mIngrese Año: \033[0m"))  
       
        libro = {
            "título": titulo,
            "autor": autor,
            "año": año,
        }
        lista_libros[contador_id] = libro
        print(f"\n\033[1m\033[32mLibro agregado con ID {contador_id}\033[0m")  
        contador_id += 1

    elif opciones == 2:
       if lista_libros:
        print(f"\n\033[1m\033[36m{'ID':<5} {'Título':<30} {'Autor':<25} {'Año':<6}\033[0m")
        print("\033[34m" + "-" * 70 + "\033[0m")
        
        for clave in lista_libros:
            libro = lista_libros[clave]
            print(
                f"\033[1m{clave:<5} "
                f"\033[1m{libro['título']:<30} "
                f"\033[1m{libro['autor']:<25} "
                f"\033[1m{libro['año']:<6}"
            )
    