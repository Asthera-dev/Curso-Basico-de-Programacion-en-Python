# Diferencia de conjuntos

La diferencia de conjuntos se utiliza para encontrar los elementos que pertenecen a un conjunto, pero no a otro.

Es decir, la diferencia de dos conjuntos llamados A y B contendrá todos los elementos que están en A pero no en B.

De esta manera, Python nos retornara los elementos que pertenecen al primer conjunto y no al segundo.

En Python, existen dos alternativas para realizar la diferencia entre dos conjuntos. Utilizando el método **difference()**, o bien, el operador **' - '**.

## El método difference()

La sintaxis para utilizar el método difference() es la siguiente:

```python
conjunto_A.difference(conjunto_B)
```

Ejemplos:

```python
# Ejemplo 1:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A.difference(conjunto_B)    # {1, 2, 3}
```

El resultado representa los elementos presentes en el conjunto A y no en el conjunto B.

```python
# Ejemplo 2:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B.difference(conjunto_A)    # {8, 6, 7}
```

Ahora el resultado representa los elementos presentes en el conjunto B y no en el conjunto A.
## El operador ' - '

La sintaxis para utilizar el operador " - " es la siguiente:

```python
conjunto_A - conjunto_B
```

```python
# Ejemplo 3:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A - conjunto_B    # {1, 2, 3}
```

```python
# Ejemplo 4:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B - conjunto_A    # {8, 6, 7}
```

Como se observa, en este caso, el orden de los conjuntos importa.

Y, ¿Qué sucede cuando ambos elementos son iguales?

```python
# Ejemplo 5:

conjunto_A = {4, 5}
conjunto_B = {4, 5}

conjunto_B - conjunto_A    # set()
```

Como se observa, Python nos devuelve un conjunto vacío.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.
