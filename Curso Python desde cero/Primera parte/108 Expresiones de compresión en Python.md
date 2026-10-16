# Expresiones de compresión

Las expresiones de compresión son una construcción en Python que nos permiten crear una nueva secuencia como listas, diccionarios y conjunto.

Aplicando una operación o expresión a cada elemento de un iterable

Además, las expresiones de compresión permiten filtrar elementos en base a una condición de ser necesario.

En resumen, las expresiones de compresión son una forma concisa y legible de realizar operaciones en iterables.

Las expresiones de compresión en Python pueden ser de tres tipos principales:

\>> **Lista de Compresión:** Crea una nueva lista aplicando una expresión a cada elemento de un iterable y, opcionalmente, filtra elemento con una condición.

\>> **Conjuntos de Compresión:** Similar a las listas de compresión, pero crea un conjunto en lugar de una lista. Esto garantiza que los elementos sean únicos.

\>> **Diccionario de Compresión:** Crea un nuevo diccionario aplicando una expresión a cada elemento de un iterable para determinar tanto las claves como los valores, opcionalmente filtrando elementos.

## Sintaxis

La sintaxis para crear expresiones de compresión, es la siguiente:

```python
# Dependiendo de las llaves es lo que obtendremos:
# [] Listas
# {} Diccionarios y conjuntos. Esto dependiendo de la expresión en su interior.

# Sintaxis basica:

[expresion for elemento in iterable if condicion]
```

Simulación de ejercicio:

\>> Desarrollar un programa en Python que genere una lista con los cuadrados de los números que van del 0 al 9.

```python
# Sin utilizar expresiones de compresión
cuadrados = []
for x in range(10):
	cuadrados.append(x**2)

print(f"Sin expresiones de compresión: {cuadrados}")

# Utilizando expresiones de compresión

print(f"Con expresiones de compresión: {[x**2 for x in range(10)]}")

# Salida:

# Sin expresiones de compresión: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Con expresiones de compresión: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Ahora:

\>> Desarrollar un programa en Python que genere una lista con los cuadrados de los **números pares** que van del 0 al 9.

```python
# Sin utilizar expresiones de compresión
cuadrados = []
for x in range(10):
	if x%2 == 0:
		cuadrados.append(x**2)

print(f"Sin expresiones de compresión: {cuadrados}")

# Utilizando expresiones de compresión

print(f"Con expresiones de compresión: {[x**2 for x in range(10) if x%2 == 0]}")

# Salida:

# Sin expresiones de compresión: [0, 4, 16, 36, 64]
# Con expresiones de compresión: [0, 4, 16, 36, 64]
```

Ahora, creemos un diccionario con expresiones de compresión:

```python
print("Diccionario creado con expresiones de compresión:")

personas = [("Carlos", 30), ("Gerardo", 25), ("Maria", 35)]
diccionario_personas = {nombre:edad for nombre, edad in personas}

print(f"Diccionario de personas: {diccionario_personas}")

# Salida:

# Diccionario creado con expresiones de compresión:
# Diccionario de personas: {'Carlos': 30, 'Gerardo': 25, 'Maria': 35}
```

También podemos agregarle condiciones:

```python
print("Diccionario creado con expresiones de compresión:")

personas = [("Carlos", 30), ("Gerardo", 25), ("Maria", 35)]
diccionario_personas = {nombre:edad for nombre, edad in personas if edad >= 30}

print(f"Diccionario de personas: {diccionario_personas}")

# Salida:

# Diccionario creado con expresiones de compresión:
# Diccionario de personas: {'Carlos': 30, 'Maria': 35}
```

Cabe mencionar que estas no son todas las alternativas para las expresiones de compresión. En esta nota se detallan las básicas.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.