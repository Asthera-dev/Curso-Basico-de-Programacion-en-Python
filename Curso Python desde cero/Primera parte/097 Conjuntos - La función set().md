# Conjuntos

Un conjunto es una colección desordenada, donde cada uno de sus elementos es único, es decir, no puede haber elementos duplicados.

Al decir que un conjunto es desordenado, nos referimos a que Python no mantendrá el orden que hemos asignado a los elementos que forman parte del conjunto.

Los conjuntos pueden ser homogéneos o heterogéneos, con lo cual, los conjuntos pueden contener elementos del mismo tipo de dato, o bien, de distinto tipo de dato.

Lo que caracteriza principalmente a un conjunto es que son mutables, por tal motivo se pueden agregar y eliminar elementos después de crearlos.

Sin embargo, los elementos dentro de un conjunto no pueden ser mutables, por tal motivo un conjunto no puede contener listas, diccionarios ni otros conjuntos.

Ya que un conjunto puede contener únicamente elementos inmutables, como por ejemplo, valores enteros, valores booleanos, Strings, Tuplas y todo tipo de dato inmutable.

## Sintaxis.

La sintaxis para crear un conjunto, es la siguiente:

```python
conjunto = {} # Conjunto vacío
conjunto = {1, 2, 3, 4, 5, ...} # Conjunto homogéneo
conjunto = {"a", 1, "b", 2, (3, 4), ...} # Conjunto heterogéneo
```

Como se menciono, un conjunto no puede contener elementos mutables:

```python
conjunto = {[]}    # TypeError: unhashable type: 'list'
conjunto = {{"a": 1}}    # TypeError: unhashable type: 'dict'
conjunto = {{1,2}}    # TypeError: unhashable type: 'set'
conjunto = {"a", "b", ("a", 2, [])}    # TypeError: unhashable type: 'list'
```

### Función set()

La sintaxis para crear un conjunto utilizando la función set(), es la siguiente:

```python
conjunto = set()    # Creando un conjunto vacío
conjunto = set(objeto_iterable)    # Este método trabaja con un solo argumento que es el objeto iterable
```

Ejemplos:

```python
# Ejemplo 1:

conjunto = {5, 1, 3, 2, 4}

print(conjunto)    # {1, 2, 3, 4, 5}
```

Es importante aclarar que, aunque pareciera que Python ordena los elementos, esto no es así. Recordemos que los elementos de un conjunto esta "desordenados"

```python
# Ejemplo 2:

conjunto = {-1, 0, 5, -2, 1, 4}

print(conjunto)    # {0, 1, 4, 5, -2, -1}
```

```python
# Ejemplo 3:

conjunto = {"a", "e", "i", "o", "u"}

print(conjunto)    # {'o', 'a', 'u', 'i', 'e'}
```

```python
# Ejemplo 4:

conjunto = {"a", 5, "e", 0, "i", 2, "o", "u", -1}

print(conjunto)    # {0, 2, 'a', 5, 'o', 'i', 'u', 'e', -1}
```

```python
# Ejemplo 5:

conjunto = {5, 1, 1, 1, 3, 5}

print(conjunto)    # {1, 3, 5}
```

```python
# Ejemplo 6:

conjunto = set("hola")

print(conjunto)    # {'o', 'l', 'h', 'a'}
```

```python
# Ejemplo 7:

conjunto = set(["e", 5, "o", 0, "a", 2, -1])

print(conjunto)    # {0, 2, 'a', 5, 'o', 'e', -1}
```

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.
