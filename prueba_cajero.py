
# Inicialización de datos para un solo usuario
while True:
    numero_cuenta_usuario = input("Ingrese su número de cuenta: ")
    try:
        saldo_inicial_usuario = float(input("Ingrese su saldo inicial: $"))
        if saldo_inicial_usuario >= 0:
            cuenta_usuario = {"saldo": saldo_inicial_usuario, "movimientos": []}
            print(f"Bienvenido/a. Su cuenta {numero_cuenta_usuario} ha sido creada con un saldo de ${saldo_inicial_usuario}.")
            break
        else:
            print("El saldo inicial debe ser mayor o igual a cero.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el saldo.")

# Menú principal
while True:
    print("\nBienvenido al Cajero Automático")
    print("1. Ver Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Ver Movimientos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        saldo = cuenta_usuario["saldo"]
        print(f"Su saldo actual es: ${saldo}")

    elif opcion == "2":
        try:
            monto_deposito = float(input("Ingrese el monto a depositar: $"))
            if monto_deposito > 0:
                cuenta_usuario["saldo"] += monto_deposito
                cuenta_usuario["movimientos"].append(("Depósito", monto_deposito))
                print(f"Se han depositado ${monto_deposito} a su cuenta.")
            else:
                print("El monto a depositar debe ser mayor que cero.")
        except ValueError:
            print("Monto inválido. Por favor, ingrese un número.")

    elif opcion == "3":
        try:
            monto_retiro = float(input("Ingrese el monto a retirar: $"))
            saldo_actual = cuenta_usuario["saldo"]
            if monto_retiro > 0 and monto_retiro <= saldo_actual:
                cuenta_usuario["saldo"] -= monto_retiro
                cuenta_usuario["movimientos"].append(("Retiro", -monto_retiro))
                print(f"Se han retirado ${monto_retiro} de su cuenta.")
            elif monto_retiro <= 0:
                print("El monto a retirar debe ser mayor que cero.")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Monto inválido. Por favor, ingrese un número.")

    elif opcion == "4":
        movimientos = cuenta_usuario["movimientos"]
        if movimientos:
            print("\nHistorial de Movimientos:")
            for movimiento, monto in movimientos:
                if monto > 0:
                    print(f"- {movimiento}: +${monto}")
                else:
                    print(f"- {movimiento}: ${monto}")
        else:
            print("No hay movimientos registrados para esta cuenta.")

    elif opcion == "5":
        print("Gracias por utilizar el Cajero Automático.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")