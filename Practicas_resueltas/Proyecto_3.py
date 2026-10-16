"""
Proyecto #3 - Tienda virtual

Crea un programa que simule una tienda virtual simple, con las siguientes especificaciones:

* Muestra un catálogo de productos disponibles con sus nombres y precios.
* El usuario deberá tener la opción de agregar productos al carrito.
* El usuario deberá tener la opción de ver lo que hay en el carrito.
* El usuario deberá tener la opción de realizar el pago y salir
"""

# Definimos el inventario
inventario = {  "Camiseta": 20,
                "Jeans": 40,
                "Zapatos": 50,
                "Sombrero": 10}

# Definimos el carrito de compras y el total a pagar
carrito = {}
total = 0

# Creamos la impresion predeterminada del menú
menu = """
============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir
"""

# Creamos la logica del programa
print("== Bienvenido a la Tienda Virtual ==")

while True:
    print(menu)
    try:
        opcion = int(input(">> Seleccione una opción: "))
    except ValueError:
        print("\n¡Error! Debe ingresar un número valido.")
        continue

    # Dependiendo de la acción ingresada, será la acción:
    match opcion:
        # Agregar productos al carrito
        case 1:
            print("\n====== AGREGAR PRODUCTOS ======")
            # Imprimimos los productos disponibles
            print("\nProductos disponibles:")
            for producto, precio in inventario.items():
                print(f"* {producto}: ${precio}")

            # Pedimos el producto
            producto = input("\n>> Ingrese el nombre del producto que desea agregar: ").capitalize().strip()

            # Verificamos que el producto exista en el inventario
            if producto in inventario:
                # Si el producto no esta en el carrito, agregamos 1 pieza
                if producto not in carrito:
                    carrito[producto] = 1

                # Si el producto ya existia, agregamos 1 unidad mas
                else:
                    carrito[producto] += 1

                # Actualizamos el total a pagar
                total += inventario[producto]
                
                print(f"\n¡{producto} agregado al carrito!")
            else:
                print("\n¡Producto no encontrado!")

        # Ver carrito
        case 2:
            print("\n====== CARRITO DE COMPRAS ======")
            # Verificamos que el carrito no esté vacío
            if carrito:
                # Imprimimos los productos en el carrito
                for producto, cantidad in carrito.items():
                    print(f"* {cantidad} - {producto}: ${inventario[producto]} c/u")
                
                print(f"\nTotal a pagar: ${total}")
            else:
                print("\nEl carrito está vacío.")

        # Pagar y salir
        case 3:
            print("\n====== PAGO ======")
            # Verificamos que el carrito no esté vacío
            if carrito:
                print(f"\nTotal a pagar: ${total}")
                
                # Solicitamos el monto a pagar
                try:
                    monto = float(input("\n>> Ingrese el monto a pagar: "))
                except ValueError:
                    print("\n¡Error! Debe ingresar un número valido.")
                    continue
                
                # Verificamos que el monto no sea demasiado grande
                if monto > total + 1000:
                    print("\n\n¡Vaya! Ha pagado demasiado. Por favor intente con una cantidad menor.")
                    continue

                # Verificamos que el monto sea exacto
                elif monto == total:
                    print("\n¡Gracias por su compra!")
                    break

                # Verificamos que el monto sea suficiente
                elif monto >= total:
                    vuelto = monto - total
                    print(f"\nSu cambio es: ${vuelto}")
                    print("\n¡Gracias por su compra!")
                    break

                else:
                    print("\n¡Monto insuficiente!")
            else:
                print("\nNo se puede pagar, el carrito está vacío.")

        # Salir del programa
        case 4:
            # Verificamos si hay productos en el carrito
            if carrito:
                print("\n¿Esta seguro que desea salir? Tiene objetos en su carrito")

                # Solicitamos confirmacion
                confirmacion = input("\n>> Confirme la acción (Si/No): ").lower().strip()

                # Si confirma, sale del programa
                if confirmacion == "si":
                    print("\n¡Hasta luego!")
                    break

                # En caso contrario, vuelve al menú
                else:
                    continue
            else:
                print("\n¡Hasta luego!")
                break

        # Opción invalida
        case _:
            print("\n¡Opción invalida!")