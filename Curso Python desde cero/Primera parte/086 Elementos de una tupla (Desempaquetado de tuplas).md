# Desempaquetado de tuplas

Una manera interesante de acceder a los elementos de una tupla es mediante el desempaquetado de tuplas. 

Esta alternativa nos permite asignar cada elemento de una tupla a una variable independiente.

## Sintaxis

La sintaxis para desempaquetar una tupla es la siguiente:

```python
var_1, var_2 = nombre_tupla[0:2]
```

Es importante mencionar que, para que el desempaquetado de tuplas funcione, la cantidad de variables debe ser igual a la cantidad de elementos contenidos en la tupla.

Ejemplos:

Cuando tenemos un control correcto de nuestro desempaquetado:

```python
# Ejemplo 1:

tupla_vocales = ("a", "e", "i", "o", "u")

v1, v2, v3 = tupla_vocales[:3]

print(v1, v2, v3)    # Salida: a e i
```

Cuando tenemos un control incorrecto de nuestro desempaquetado:

```python
# Ejemplo 2 (Variables insuficientes):

tupla_vocales = ("a", "e", "i", "o", "u")

v1, v2, v3 = tupla_vocales[:4]

# Salida: ValueError: too many values to unpack (expected 3)
```

```python
# Ejemplo 3 (Numero excesivo de variables):

tupla_vocales = ("a", "e", "i", "o", "u")

v1, v2, v3, v4 = tupla_vocales[:3]

# Salida: ValueError: not enough values to unpack (expected 4, got 3)
```

Como se observa, Python nos marcará siempre un error cuando el número de variables dadas sea insuficiente o excesivo.

Finalmente:

> Se recomienda practicar este tema creando sus propias tuplas y programas. Esto con el objetivo de lograr una compresión más profunda del tema.

