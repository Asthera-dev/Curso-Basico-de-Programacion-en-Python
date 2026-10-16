# Función enumerate()

La función enumerate() se utiliza para recorrer elementos de un objeto iterable, como listas, tuplas o Strings, al mismo tiempo que se lleva un contador de la posición de cada elemento.

Lo cuall es de gran utilidad cuando necesitamos saber la posición de un elemento mientras se recorre la secuencia.

## Sintaxis

La sintaxis para utilizar la función enumerate() es la siguiente:

```python
enumerate(objeto_iterable) # Trabajando con un argumento
enumerate(objeto_iterable, start = 0) # Trabajando con dos argumentos
```

Donde **start** representa el número desde el que empezara a contar el método.

Ejemplo:

```python
# Trabajando con un argumento

frutas = ["manzana", "platano", "uva", "sandía"]
print(frutas)

print("\nRecorrido con for:")

for posicion, fruta in enumerate(frutas):
	print(f"Posición {posicion}: {fruta}")

# Salida:

# ['manzana', 'platano', 'uva', 'sandía']

# Recorrido con for:
# Posición 0: manzana
# Posición 1: platano
# Posición 2: uva
# Posición 3: sandía
```

```python
# Trabajando con un ambos argumentos:

frutas = ["manzana", "platano", "uva", "sandía"]
print(frutas)

print("\nRecorrido con for:")

for posicion, fruta in enumerate(frutas, 100):
	print(f"Posición {posicion}: {fruta}")

# Salida:

# ['manzana', 'platano', 'uva', 'sandía']

# Recorrido con for:
# Posición 100: manzana
# Posición 101: platano
# Posición 102: uva
# Posición 103: sandía
```

Como se observa, con el método for podemos acceder uno a uno a los elementos de las lista y enumerarlos. Pero también podemos obtener una lista con este método:

```python
print("Convirtiendo a lista")
print(list(enumerate(frutas))) 
print(list(enumerate(frutas, start = 1))) 

# Salida: 

# Convirtiendo a lista
# [(0, 'manzana'), (1, 'platano'), (2, 'uva'), (3, 'sandía')]
# [(1, 'manzana'), (2, 'platano'), (3, 'uva'), (4, 'sandía')]
```

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.