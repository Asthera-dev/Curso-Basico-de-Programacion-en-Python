# La función tuple()

La función tuple() permite crear una tupla a partir de una secuencia, como por ejemplo, una lista, una cadena o un rango, es decir, con ayuda de esta función, es posible convertir un objeto iterable en una tupla.

## Sintaxis

La sintaxis para utilizar la función tuple() es la siguiente:

```python
# Esta función, al igual que el constructor list() solo trabaja con un argumento:

tuple(objeto_iterable)
```

Ejemplos:

```python
# Ejemplo 1 (Trabajando con coordenadas):

x = 10
y = 5

coordenada = tuple(x, y)

# Salida: TypeError: tuple expected at most 1 argument, got 2
```

Esto ocurre porque, como se menciono, la función tuple() solo acepta un argumento y ese argumento debe ser un objeto iterable.

```python
# Ejemplo 2 (Trabajando con coordenadas):

x = 10
y = 5

coordenada = tuple([x, y])

print(coordenada)

# Salida: (10, 5)
```

Como nuestras coordenadas **'x'** & **'y'** ahora son una lista, y una lista es un objeto iterable, la función tuple() puede trabajar sin mayor problema.

```python
# Ejemplo 2 (Trabajando con Strings):

texto = "Hola"

tupla_de_string = tuple(texto)

print(tupla_de_string)

# Salida: ('H', 'o', 'l', 'a')
```

Ahora, como la palabra 'Hola' es un objeto iterable, la función tuple() convertirá cada elemento de esta palabra en un elemento de la tupla.

```python
# Ejemplo 2 (Trabajando con un diccionario):

numbers_dict = {"uno": 1,
				"dos": 2,
				"tres": 3
				} 

tupla_claves = tuple(numbers_dict)

print(tupla_claves)

# Salida: ('uno', 'dos', 'tres')
```

Aquí, al ejecutar este código, la tupla resultante contendrá solo las claves de nuestro diccionario.

> Se recomienda practicar este tema creando sus propias tuplas y programas. Esto con el objetivo de lograr una compresión más profunda del tema.

