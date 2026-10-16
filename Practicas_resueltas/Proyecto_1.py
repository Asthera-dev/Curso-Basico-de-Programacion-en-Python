"""
Proyecto #1 - Adivina el número

Desarrollar un juego interactivo llamado "Adivina el número secreto"

El programa seleccionará aleatoriamente un número entre un rango especificado
y el jugador deberá adivinar el "número secreto" en un número limitado de intentos.

Requisitos
1. Seleccionar un número aleatorio entre 1 y 100.
2. El jugador tiene 10 intentos para adivinar el número.
3. El programa debe indicar si el número introducido es mayor o menor al número secreto.
4. Mostrar cuántos intentos le quedan al jugador.
5. Al finalizar el juego, mostrar un mensaje indicando si adivinó el número o no.
6. Si adivina el número, mostrar en qué intento lo logró.
7. Si se agotan los intentos, mostrar el número secreto.
8. El programa debe permitir volver a jugar.

Requerimientos indispensables:
* El programa debe contener un manejo de expeciones que evite errores ante entradas no
  validas del usuario (ej: letras, números decimales, etc).

Extensión (Opcional)
- Guardar un registro de las mejores puntuaciones.
- Implementar diferentes niveles de dificultad con rangos de números y cantidad de intentos variables.
- Incluir un sistema de pistas.
- Permitir jugar con números negativos.
"""
# Importamos el modulo randint de la libreria random:
from random import randint

# Iniciamos el juego seleccionando el número a encontrar:
numero_secreto = randint(0, 100) # Elegimos un número aleatorio entre 0 y 100.
intentos = 10 # Establecemos la cantidad de intentos permitidos.

# Imprimimos un mensaje de bienvenida:
print("¡Bienvenido al juego Adivina el número!")
print("He pensado en un número entre 0 y 100. ¿Puedes adivinarlo?")
print(f"Tienes {intentos} intentos para adivinar el número.")

# Empezamos el juego
n = 0 # Definimos el "contador" de intentos.
numero_usuario = None # Inicializamos la variable con un valor que no sea el número secreto para evitar errores al final del juego.

while n < intentos:
    n += 1 # Sumamos un intento por cada vuelta. Aún si el usuario ingreso un dato invalido.

    # Utilizamos el manejo de excepciones para soliciar un número al usuario de forma segura:
    try:
        numero_usuario = int(input(f"\nIntento {n}/{intentos}\nIngresa un número: "))

    except ValueError: # Manejamos la excepción de que el usuario ingrese un valor no válido de tipo String.
        print("Error: Debes ingresar un número entero.")
        continue

    # Creamos la lógica del juego:
    if numero_usuario == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {n} intentos")
        break # Termina el bucle si adivinó

    # Si no adivinó, indicamos si el número es mayor o menor
    elif numero_usuario < numero_secreto:
        print("El número secreto es mayor.")
    elif numero_usuario > numero_secreto:
        print("El número secreto es menor.")

# Si el usuario no adivina el número secreto al terminar los intentos, se ejecuta el siguiente bloque:
if numero_usuario != numero_secreto:
    print(f"\nLo siento, has agotado tus intentos. El número secreto era {numero_secreto}")