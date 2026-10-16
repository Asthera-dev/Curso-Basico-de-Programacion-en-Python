"""
Programa de "modificación de tupla"

Escribe un programa en Python que realice lo siguiente:

1. Muestre la tupla original a través de una impresión en pantalla.
2. Solicitar al usuario ingresar un número existente dentro de la tupla.
3. Buscar en la tupla el número ingresado y remplazarlo por 0.
4. Mostrar la tupla modificada a través de una impresión en pantalla.
"""

# Tupla base

nums_tuple = (5, 8, 3, 3, 1, 6, 2)

# 1. Imprimimos la tupla original

print(f"Tupla original: {nums_tuple}")

# 2. Solicitamos al usuario un número existente dentro de la tupla

numero = int(input(">>> ¿Cúal de estos números quieres modificar por 0?:"))

# 3. Buscamos en la tupla el número ingresado y lo remplazamos por 0:

new_tuple = []
for i in nums_tuple:
    if i == numero:
        new_tuple.append(0)
    else:
        new_tuple.append(i)

# 4. Mostramos la tupla modificada a través de una impresión en pantalla:

print(f"Tupla modificada (Algoritmo 1): {tuple(new_tuple)}")

####################################################################

# Forma 2 (con listas por comprensión):

new_tuple_2 = [0 if i == numero else i for i in nums_tuple]

print(f"Tupla modificada (Algoritmo 2): {tuple(new_tuple_2)}")