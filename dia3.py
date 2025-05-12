# Inventory dictionary to store product information
inventory = {}

def add_initial_products(inventory_local):
    """Adds 5 initial products to the inventory."""
    add_another = True # Flag to control the loop
    product_count = 0 # Counter for added products
    product_number = 1 # Counter for product numbering in input prompts
    print("\n\033[94m\033[1m---Añadir 5 productos iniciales para continuar la gestion del inventario----\033[0m")
    while add_another:
        product_name = input(f"\n\033[1mIngrese el nombre del producto # {product_number}: ").strip() # Get product name
        if product_name in inventory_local: # Check if product already exists
            print(f"\n\033[93m El producto '{product_name}' ya existe\033[0m")
            continue # Go to the next iteration

        product_number = product_number + 1 # Increment product number
        product_count = product_count + 1 # Increment product count
        while True:
            try:
                price_str = input("\n\033[1mIngrese el precio del producto: ").replace(',', '.') # Get price input
                price = float(price_str) # Convert price to float
                if price < 0: # Check if price is positive
                    print("\n\033[93m El precio debe ser un valor positivo.\033[0m")
                    continue # Ask for price again
                break # Exit price input loop
            except ValueError:
                print("\n\033[93m Ingrese un numero valido para el precio.\033[0m") # Handle invalid input

        while True:
            try:
                quantity_str = input("\n\033[1mIngrese la cantidad disponible: ") # Get quantity input
                quantity = int(quantity_str) # Convert quantity to integer
                if quantity < 0: # Check if quantity is positive
                    print("\n\033[93m La cantidad debe ser un valor positivo.\033[0m")
                    continue # Ask for quantity again
                break # Exit quantity input loop
            except ValueError:
                print("\n\033[93m Ingrese un numero entero valido para la cantidad.\033[0m") # Handle invalid input

        inventory_local[product_name] = {'precio': price, 'cantidad': quantity} # Add product to inventory
        print(f"\n\033[1m\033[32mEl producto '{product_name}' ha sido añadido al inventario.\033[0m")

        if product_count == 5: # Check if 5 products have been added
            add_another = False # Stop the loop

def add_product(inventory_local):
    """Adds a new product to the inventory."""
    print("\n\033[94m\033[1mAñadir Producto\033[0m")
    product_name = input("\n\033[1mIngrese el nombre del producto: ").strip() # Get product name
    if product_name in inventory_local: # Check if product exists
        print(f"\n\033[93m El producto '{product_name}' ya existe\033[0m")
        return # Exit the function
    while True:
        try:
            price_str = input("\n\033[1mIngrese el precio del producto: ").replace(',', '.') # Get price input
            price = float(price_str) # Convert to float
            if price < 0: # Check for positive price
                print("\n\033[93m El precio debe ser un valor positivo.\033[0m")
                continue # Ask again
            break # Exit loop
        except ValueError:
            print("\n\033[93m Ingrese un numero valido para el precio.\033[0m") # Handle invalid input

    while True:
        try:
            quantity_str = input("\n\033[1mIngrese la cantidad disponible: ") # Get quantity input
            quantity = int(quantity_str) # Convert to integer
            if quantity < 0: # Check for positive quantity
                print("\n\033[93m La cantidad debe ser un valor positivo.\033[0m")
                continue # Ask again
            break # Exit loop
        except ValueError:
            print("\n\033[93m Ingrese un numero entero valido para la cantidad.\033[0m") # Handle invalid input

    inventory_local[product_name] = {'precio': price, 'cantidad': quantity} # Add product to inventory
    print(f"\n\033[1m\033[32mEl producto '{product_name}' ha sido añadido al inventario.\033[0m")

def consult_product(inventory_local):
    """Consults and displays the information of a product in the inventory."""
    print("\n\033[94m\033[1mConsultar Producto\033[0m")
    product_name = input("\n\033[1mIngrese el nombre del producto que desea consultar: ").strip() # Get product name to consult
    if product_name in inventory_local: # Check if product exists
        product_info = inventory_local[product_name] # Get product information
        price = product_info['precio'] # Get price
        quantity = product_info['cantidad'] # Get quantity
        print("\n")
        print("\033[1m" + "-" * 30 + "\033[0m")#formatting
        print(f"\033[1m| \033[94m{'Producto':<15} \033[0m| {product_name:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")#formatting
        print(f"\033[1m| \033[94m{'Precio':<15}\033[0m | ${price:11,.2f} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")#formatting
        print(f"\033[1m|\033[94m {'Cantidad':<15}\033[0m | {quantity:<12} |\033[0m")
        print("\033[1m" + "-" * 30 + "\033[0m")
    else:
        print(f"\033[93m El producto '{product_name}' no se encuentra en el inventario.\033[0m") # Product not found

def update_price(inventory_local):
    """Updates the price of an existing product in the inventory."""
    print("\n\033[94m\033[1mActualizar Precio\033[0m")
    product_name = input("\n\033[1mIngrese el nombre del producto cuyo precio quiere actualizar: ").strip() # Get product name to update
    if product_name in inventory_local: # Check if product exists
        while True:
            try:
                new_price_str = input("\n\033[1mIngrese el nuevo precio: ").replace(',', '.') # Get new price input
                new_price = float(new_price_str) # Convert to float
                if new_price < 0: # Check for positive price
                    print("\n\033[93mEl precio debe ser un valor positivo.\033[0m")
                    continue # Ask again
                inventory_local[product_name]['precio'] = new_price # Update the price
                print(f"\n\033[1m\033[32mEl precio de '{product_name}' ha sido actualizado a ${new_price:,.2f}.\033[0m")
                break # Exit loop
            except ValueError:
                print("\n\033[93mPor favor, ingrese un numero valido para el precio.\033[0m") # Handle invalid input
    else:
        print(f"\n\033[93m El producto '{product_name}' no se encuentra en el inventario.\033[0m") # Product not found

def delete_product(inventory_local):
    """Deletes a product from the inventory."""
    print("\n\033[94m\033[1mEliminar Producto\033[0m")
    product_name = input("\033[1mIngrese el nombre del producto que quiere eliminar: ").strip() # Get product name to delete
    if product_name in inventory_local: # Check if product exists
        del inventory_local[product_name] # Delete the product
        print(f"\n\033[1m\033[31mEl producto '{product_name}' ha sido eliminado.\033[0m")
    else:
        print(f"\n\033[93m El producto no se encuentra en el inventario.\033[0m") # Product not found

def calculate_total_value(inventory_local):
    """Calculates and displays the total value of the inventory."""
    print("\n\033[94m\033[1mValor Total del Inventario\033[0m")
    total_value_lambda = lambda inventory: sum(product['precio'] * product['cantidad'] for product in inventory.values()) # Lambda to calculate total value
    total_value = total_value_lambda(inventory_local) # Calculate total value
    print(f"\n\033[1mEl valor total del inventario es: ${total_value:,.2f}\033[0m")
    return

def display_inventory(inventory_local):
    """Displays the current inventory with product names, prices, and quantities."""
    print("\n\033[94m\033[1mMostrar Inventario\033[0m")
    if not inventory_local: # Check if inventory is empty
        print("\033[1m\n\033[93m\El inventario está vacio.\033[0m")
        return
    print("\n\033[94m\033[1mInventario Actual: \033[0m")
    product_index = 0 # Initialize product index
    for product_name, product_info in inventory_local.items(): # Iterate through inventory
        product_index = product_index + 1 # Increment index
        price = product_info['precio'] # Get price
        quantity = product_info['cantidad'] # Get quantity
        print(f"\n\033[1mProducto({product_index}): {product_name}, Precio: ${price:,.2f}, Cantidad: {quantity}\033[0m")
    print("-" * 35)


add_initial_products(inventory) # Add initial products
while True:

    print("\n\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[94m\033[1m" + "  SISTEMA DE INVENTARIO  ".center(35) + "\033[0m")
    print("\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[1m  Opciones:\033[0m")
    print(f"\033[1m  1. Añadir producto{''.ljust(31)}\033[0m")
    print(f"\033[1m  2. Consultar producto{''.ljust(29)}\033[0m")
    print(f"\033[1m  3. Actualizar precio{''.ljust(30)}\033[0m")
    print(f"\033[1m  4. Eliminar producto{''.ljust(30)}\033[0m")
    print(f"\033[1m  5. Calcular valor total del inventario{''.ljust(24)}\033[0m")
    print(f"\033[1m  6. Mostrar inventario{''.ljust(27)}\033[0m")
    print(f"\033[1m  7. Salir{''.ljust(34)}\033[0m")
    print("\033[94m" + "═" * 35 + "\033[0m")

    option = input("\033[94m\033[1mSeleccione una opcion: \033[0m")# Get user option
    if option == '1':
        add_product(inventory) # Call add product function
    elif option == '2':
        consult_product(inventory) # Call consult product function
    elif option == '3':
        update_price(inventory) # Call update price function
    elif option == '4':
        delete_product(inventory) # Call delete product function
    elif option == '5':
        total_value = calculate_total_value(inventory) # Call calculate total value function
    elif option == '6':
        display_inventory(inventory) # Call display inventory function
    elif option == '7':
        print("\n\033[94m\033[1mSaliendo del programa\033[0m") # Exit message
        break # Exit the main loop
    else:
        print("\n\033[93m Opcion invalida. seleccione una opcion valida.\033[0m") # Invalid option message
