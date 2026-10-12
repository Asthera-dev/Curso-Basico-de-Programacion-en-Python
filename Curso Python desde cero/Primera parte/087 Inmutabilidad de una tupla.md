# Inmutabilidad de una tupla

La inmutabilidad de las tuplas es una característica fundamental que impide tanto la modificación de sus elementos así como de su longitud después de haber sido creada.

Esto significa que, una vez creada la tupla, sus elementos son fijos y no pueden ser alterados directamente.

La inmutabilidad de las tuplas es útil en situaciones donde se necesita garantizar que ciertos datos permanezcan constantes durante la ejecución de un programa.

No obstante, si un elemento dentro de una tupla es mutable, como por ejemplo las listas o los diccionarios, existe cierta flexibilidad al permitir la modificación de los elementos internos, aunque la tupla en si misma sigue siendo inmutable. 

Ejemplos:

```python
# Ejemplo 1 (Error de asignación): 

nums_tuple = (1, 2, 3, 4, 5)

nums_tuple[0] = 0

# Salida: TypeError: 'tuple' object does not support item assignment
```

Ahora veamos la modificación de estructura de datos dentro de una tupla:

```python
# Ejemplo 2 (Error de asignación): 

nums_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3,2))

nums_tuple[0] = 2

# Salida: TypeError: 'tuple' object does not support item assignment
```

```python
# Ejemplo 2 (modificación de estructura de datos): 

nums_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3,2))

nums_tuple[0][1] = 99
nums_tuple[1]["dos"] = 98

print(nums_tuple)

# Salida: ([1, 99, 3], {'uno': 1, 'dos': 98}, (3, 2))
```

Como se observa, no se puede modificar la tupla, si embargo, si se pueden modificar otras estructuras de datos que contenga en su interior.

Finalmente:

> Se recomienda practicar este tema creando sus propias tuplas y programas. Esto con el objetivo de lograr una compresión más profunda del tema.