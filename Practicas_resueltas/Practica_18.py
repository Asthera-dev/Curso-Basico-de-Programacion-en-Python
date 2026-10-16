"""
Programa de Suma de Tuplas

Escribe un programa en Python que realice lo siguiente:

1. Realizar la suma de ambas tuplas elemento a elementos
2. Mostrar en pantalla las tuplas originales, así como el resultado de la suma en el siguiente formato:


# Tupla 1:    (1, 2, 3, 4, 5)
#             +
# Tupla 2:    (8, 6, 4, 2, 0)
#             ===============
# Suma:       (9, 8, 7, 6, 5)


"""

# Tuplas base:

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (8, 6, 4, 2, 0)

# 1. Empezamos sumando las tuplas:

suma_tuplas = []

for i, j in zip(tuple1, tuple2):
    suma_tuplas.append(i+j)

# 2. Mostramos el resultado:


print("Tupla 1:".ljust(13), tuple1)
print("".ljust(14) + "+")
print("Tupla 2:".ljust(13), tuple2)
print("".ljust(14) + "===============")
print("Suma:".ljust(13), tuple(suma_tuplas))

