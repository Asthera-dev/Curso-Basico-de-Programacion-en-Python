# Elementos de una tupla

Para acceder a los elementos de una tupla, existen tres alternativas para hacerlo: 

1. Mediante índices.
2. [Mediante el operador de segmentación.](085%20Elementos%20de%20una%20tupla%20(operador%20de%20segmentación).md)
3. [Mediante el desempaquetado de tuplas.](086%20Elementos%20de%20una%20tupla%20(Desempaquetado%20de%20tuplas).md)

En esta nota nos enfocaremos exclusivamente en el método uno.

## Acceder mediante índices

Una forma común de acceder a los elementos de una tupla es mediante índices.

Al igual que lo hacemos con las listas, los índices nos permiten acceder a los elementos de una tupla indicando la posición del elemento a consultar.

La sintaxis para acceder a los elementos de una tupla mediante índices es la siguiente:

```python
nombre_tupla[indice] # Donde el indice es un número entero positivo o negativo
```

Ejemplos:

```python
# Ejemplo 1:

tupla_vocales = ("a", "e", "i", "o", "u")

print(tupla_vocales[3])    # Salida: o
print(tupla_vocales[1])    # Salida: e
print(tupla_vocales[-1])    # Salida: u
print(tupla_vocales[-5])    # Salida: a
```

Al igual que las listas, las tuplas pueden manejar índices positivos, que empiezan desde cero, y también índices negativos, que empiezan desde -1 y decrecen de derecha a izquierda.

Finalmente:

> Se recomienda ejecutar el programa a continuación para observar su salida. Además, también se anima al lector a modificar los valores y agregar más elementos para crear un programa más completo.

```python
countries_tuple = ("México", "Brasil", "Argentina", "España")

print(countries_tuple, "\n")

print(f"Posición 1: {countries_tuple[1]}")
print(f"Posición 3: {countries_tuple[3]}")
print(f"Posición -1: {countries_tuple[-1]}")
print(f"Posición -4: {countries_tuple[-4]}")
```

