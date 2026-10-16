"""
Proyecto #2 - Piensa en un número

Desarrollar un juego interactivo llamado "Piensa en un número"

El usuario debe ser invitado a pensar en un número secreto, y el programa intentará adivinarlo haciendo preguntas astutas.

El rango de números será del 1 al 100.

El programa debe:

- Preguntar si el número pensado es mayor, menor o correcto.
- Adivinar el número.
- Mostrar el número de intentos.
"""
# Importamos randint de random para generar numeros aleatorios
from random import randint as rd


# Definimos los parametros iniciales del juego

intentos, numero_menor, numero_mayor = 0, 0, 100
palabras_clave = ["mayor", "menor", "correcto"]

# Imprimimos un mensaje de bienvenida
print(f"""
Usuario, piensa en un número entre {numero_menor} y {numero_mayor}. Yo tratare de adivinarlo.
Para ayudarme, escribe por favor las siguientes palabras clave: {palabras_clave} """)

# Iniciamos el juego

while True:
    # Generamos un número aleatorio para empezar
    numero_maquina = rd(numero_menor, numero_mayor)

    # Bucle infinito para pedir la palabra clave al usuario
    while True: 
        # Mostramos el número aleatorio para empezar
        print(f"\n¿Es {numero_maquina} tu número?")

        # Pedimos al usuario que ingrese una de las palabras clave y lo convertimos a minúsculas y quitamos los espacios en blanco
        ayuda = input(f">> Ingresa 'mayor', 'menor' o 'correcto': ").lower().strip()
    
        # Si la palabra ingresada no está en la lista de palabras clave
        if ayuda not in palabras_clave: 
            # Mostramos un mensaje de error
            print(f"\nPor favor ingresa una de las palabras clave: {palabras_clave}.") 
            # Continuamos hasta que el usuario ingrese una palabra valida
        else:
            # Salimos del ciclo cuando el usuario ingreso una palabra valida
            break 

    # Incrementamos el número de intentos
    intentos += 1 

    # Si la palabra ingresada es "correcto"
    if ayuda == "correcto": 
        # Mostramos el número adivinado y el número de intentos
        print(f"\n¡Adiviné! Tu número es {numero_maquina}. Y lo hice en {intentos} intentos.\n\n")
        # Rompemos el ciclo
        break
    # Si el usuario no ingreso la palabra "correcto", pero el numero menor y el mayor son iguales, es porque ese es el número.
    elif numero_menor == numero_mayor:
        # Mostramos el número adivinado y el número de intentos
        print(f"\nEl número restante, segun tus pistas, es {numero_menor}. He realizado {intentos} intentos.\n\n")
        # Rompemos el ciclo 
        break
    # Si la palabra ingresada es "mayor"
    elif ayuda == "mayor": 
        # Actualizamos el número menor
        numero_menor = numero_maquina + 1
    # Si la palabra ingresada es "menor"
    elif ayuda == "menor": 
        # Actualizamos el número mayor
        numero_mayor = numero_maquina - 1

    # Verificamos si las pistas no generar un error del tipo: ValueError: empty range for randrange()
    if numero_menor > 100:
        print("\n¡Error! Tu número no puede ser mayor que 100. Verifique sus pistas")
        break
    elif numero_mayor < 0:
        print("\n¡Error! Tu número no puede ser menor que 0. Verifique sus pistas")
        break