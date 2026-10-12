# La función zip()

La función zip() se utiliza para combinar elementos de varias secuencias, como pueden ser listas, tuplas, Strings, rangos, etc. Y esta combinación se realiza en pares ordenados.

Esta función crea un iterador que produce tuplas donde el primer elemento en cada una de las secuencias dadas se empareja, luego el segundo elemento en cada una de las secuencias se empareja, y así sucesivamente.

Si las secuencias tienen longitudes diferentes, la función zip() se detendrá cuando la secuencia más corta termine.

Algo importante de mencionar, es que la función zip() devuelve un iterador, por lo que si se desea consultar el contenido generado por la función, el iterador se debe convertir a lista con la función [list()](Primera%20parte/060%20Constructor%20list()%20-%20Convertir%20objetos%20a%20listas.md), o bien, a tupla con la función [tuple()](Primera%20parte/090%20La%20función%20tuple().md).

## Sintaxis

La sintaxis para utilizar la función zip() es la siguiente:

```python
zip(objeto_iterable, objeto_iterable, ...)
```

Ejemplos:

```python
# Ejemplo 1:

names = ("Luis", "Diego", "Andrés", "Carlos")
ages = [15, 30, 26, 12, 40]

combination = zip(names, ages)

print(combination)    # Salida: <zip object at 0x00000...........>

combination = list(combination)

print(combination)    # Salida: [('Luis', 15), ('Diego', 30), ('Andrés', 26), ('Carlos', 12)]

```