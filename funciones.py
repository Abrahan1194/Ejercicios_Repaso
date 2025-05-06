def ejercicio_1 ():
    nombre = input("ingrese nombre : ")
    print(f"Hola coder , bienvenido a riwi {nombre}")


def ejercicio_2 ():
    num1 = int(input("ingrese numero 1 :"))
    num2 = int(input("ingrese numero 2 :"))
    suma = num1+num2
    print(f"La suma es : {suma}")

def ejercicio_3 ():
    numero =  int(input("Ingrese un número: "))
    if numero  % 2 == 0:
       print(numero, "es par.")
    else:
      print(numero, "es impar.")


def ejercicio_4 ():
  edad = int(input("Por Favor Dame Tu edad: "))
  if edad >= 18 : 
    print("Eres mayor de edad")
  else:
   print("Eres menor de edad")

def ejercicio_5 ():
  grados_celsius = int(input("Por Favor, Ingrese Grados celsius: "))
  fahrenheit = (grados_celsius * 9/5) + 32.
  print(f"{grados_celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

def ejercicio_6 ():
  base = int(input("Ingrese base del triagulo : "))
  altura = int(input("Ingrese altura del triagulo : "))
  area = (base * altura) / 2
  print(f"El area es : {area}")

def ejercicio_7 ():
   lista_numeros = []
   i = 0
   for i in range(4) :
    numeros = int(input("Ingrese Numero : "))
    lista_numeros.append(numeros)
    i = i+1
   
   if lista_numeros :
    print(f"Numero mayor es : {max(lista_numeros)}")

def ejercicio_8():
  palabra = input("Ingrese una palabra: ")
  letra_a_contar = input("Ingrese la letra a contar: ")
  contador = 0

  for letra in palabra:
    if letra == letra_a_contar:
        contador += 1

  print("La letra '" + letra_a_contar + "' aparece " + str(contador) + " veces en la palabra.")

def ejercicio_9():
 numeros = input("Ingrese una lista de números separados por espacios: ").split()
 pares = []

 for numero in numeros:
    if int(numero) % 2 == 0:
        pares.append(int(numero))

 print("Números pares:", pares)


def ejercicio_10():
    palabra = input("Ingrese una palabra: ")
    palabra_limpia = "".join(palabra.lower().split())  # Eliminar espacios y convertir a minúsculas
    palindromo = palabra_limpia == palabra_limpia[::-1]

    if palindromo:
        print("La palabra ingresada es un palindromo")
    else:
        print("La palabra ingresada no es un palindromo")

def ejercicio_11(): 
    numero = int(input("Introduce un numero: "))
    factorial = 1
    if numero < 0:
        print("El factorial no esta definido para numeros negativos")
    elif numero == 0:
        print("El factorial de 0 es 1")
    else:
        for i in range(1, numero + 1):
            factorial *= i
        print("El factorial de", numero, "es", factorial)

def ejercicio_12():
  numeros1 = float(input("Ingrese una lista de números separados por espacios: ").split())
  iguales = []
  for num in numeros1 :
     if int(num) == 
     

