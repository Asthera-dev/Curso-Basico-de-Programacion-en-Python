"""
Programa "Seleccionador" de nombres

Escribe un programa en Python que realice lo siguiente:
1. Muestre la tupla a través de una impresión en pantalla.
2. Solicitar al usuario ingresar un número entero entre 0 y 4
3. Si el número ingresado es válido (entre 0 y 4) el programa muestra el nombre correspondiente al índice ingresado en la tupla y finaliza.
4. Sí el número ingresado no esta en el rango válido (entre 0 y 4), el programa muestra un mensaje de error y vuelve a solicitar al usuario que ingrese un número.
"""

# Tupla base:

names_tuple = ("Ana", "Gerardo", "María", "Carlos", "Valentina")

# 1 Mostramos la tupla:

print(f"Tupla original: {names_tuple}")

# 2 y 3. Solicitamos al usuario un índice y lo validamos:

while True:
    numero = int(input("\n>>> Introduce un número entero entre 0 y 4: "))
    
    if 0 <= numero <= 4:
        print(f"\nEl nombre correspondiente al índice {numero} es: {names_tuple[numero]}")
        break
    else:
        print("\n¡Error!: Número invalido, vuelve a intentar.")