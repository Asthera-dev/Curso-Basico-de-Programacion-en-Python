"""
Programa de ordenamiento de una tupla.

Escribe un programa en Python que realice lo siguiente:

1. Mostrar la tupla original a través de una impresión en pantalla
2. Mostrar en pantalla, la información de la persona de menor edad y la de mayor edad.
"""

# Tupla base:
personas = (("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22))

# 1. Mostrando la tupla original:

print(f"Personas: {personas}\n")

# 2. Ordenamos la tupla por edad:

personas = list(personas)


for i in range(len(personas)):
    for j in range(i + 1, len(personas)):

        if personas[i][1] > personas[j][1]:
            auxiliar = personas[i]
            personas[i], personas[j] = personas[j], auxiliar



print(f"Menor edad: {personas[0]}")
print(f"Mayor edad: {personas[-1]}")


# Representación grafica del funcionamiento del algoritmo anterior

"""
Arreglo original
(("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22))

# Tras convertirlo a lista:
[("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22)]

# Primera iteración:

i = 0
j = 1
personas[i][1] = 26 ---> ("Eduardo", 26)
personas[j][1] = 30 ---> ("María", 30)

26 > 30 = False

# Segunda iteración:

i = 0
j = 2
personas[i][1] = 26 ---> ("Eduardo", 26)
personas[j][1] = 20 ---> ("Gerardo", 20)

26 > 20 = True

auxiliar = personas[i] ---> ("Eduardo", 26)
personas[i], personas[j] = personas[j], auxiliar ---> ("Gerardo", 20), ("Eduardo", 26)

# Tercera iteración:

personas = [("Gerardo", 20), ("María", 30), ("Eduardo", 26), ("Valentina", 22)]

i = 0
j = 3
personas[i][1] = 20 ---> ("Gerardo", 20)
personas[j][1] = 22 ---> ("Valentina", 22)

20 > 22 = False

# Cuarta iteración:

i = 1
j = 2
personas[i][1] = 30 ---> ("María", 30)
personas[j][1] = 26 ---> ("Eduardo", 26)

30 > 26 = True

auxiliar = personas[i] ---> ("María", 30)
personas[i], personas[j] = personas[j], auxiliar ---> ("Eduardo", 26), ("María", 30)

# Quinta iteración:

personas = [("Gerardo", 20), ("Eduardo", 26), ("María", 30), ("Valentina", 22)]

i = 1
j = 3
personas[i][1] = 26 ---> ("Eduardo", 26)
personas[j][1] = 22 ---> ("Valentina", 22)

26 > 22 = True

auxiliar = personas[i] ---> ("Eduardo", 26)
personas[i], personas[j] = personas[j], auxiliar ---> ("Valentina", 22), ("Eduardo", 26)

# Sexta iteración:

personas = [("Gerardo", 20), ("Valentina", 22), ("María", 30), ("Eduardo", 26)]

i = 2
j = 3
personas[i][1] = 30 ---> ("María", 30)
personas[j][1] = 26 ---> ("Eduardo", 26)

30 > 26 = True

auxiliar = personas[i] ---> ("María", 30)
personas[i], personas[j] = personas[j], auxiliar ---> ("Eduardo", 26), ("María", 30)

# Séptima iteración:

personas = [("Gerardo", 20), ("Valentina", 22), ("Eduardo", 26), ("María", 30)]

i = 3
j = 4

Como el segundo for esta definido por (i + 1) hasta range(len(personas)):
>> En este ciclo el valor seria 4 hasta 3. Recordemos que range() no incluye el stop (4 en este caso)
>> Como el valor de inicio es mayor que el de fin, el ciclo no se ejecutaria. Pero tampoco causara un error.
>> En resumen, no hay séptima iteración.

Fin del algoritmo.

Lista final resultante:
[("Gerardo", 20), ("Valentina", 22), ("Eduardo", 26), ("María", 30)]
"""
