# Programa que crea una matriz desde teclado y la muestra

matriz = []

filas = 3 # int(input(">>¿Cuantas filas tendra su matriz?: "))
columnas = 3 # int(input(">>¿Cuantas columnas tendra su matriz?: "))

# ==================================================================================================
# Primer algoritmo:

# Iniciamos el ciclo for que creara las filas de nuestra matriz
for fila in range(filas):
    matriz.append([]) # Añadimos una lista vacia a nuestra matriz

    # Iniciamos el segundo ciclo for que creara las columnas de nuestra matriz
    for columna in range(columnas):
        numero = int(input(f">>Ingrese un numero para la fila {fila} y columna {columna}: "))
        matriz[fila].append(numero)

    # Añadimos un salto de línea para comodidad del usuario
    print()

# ==================================================================================================
# Segundo algoritmo:

# Iniciamos el primer for que creara las filas de la matriz
for fila_posicion in range(filas):
    fila = [] # Creamos una lista vacia para almacenar los elementos de la fila
    
    # Iniciamos el segundo for que creara las columnas de la matriz
    for elemento in range(columnas):
        fila.append(int(input(f">>Ingrese un numero para la fila {fila_posicion} y columna {elemento}: ")))
    matriz.append(fila)
    print()

# ==================================================================================================


# Creamos el for que mostrara la matriz resultante

for fila in matriz:
    print(fila)
