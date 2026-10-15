# Intersección de conjuntos

La intersección entre conjuntos es una operación que permite encontrar elemento en común, entre dos conjuntos.

En Python, existen dos alternativas para realizar la intersección entre dos conjuntos. Utilizando el método **intersection()**, o bien, utilizando el operador **'&'**.

## El método intersection()

La sintaxis para utilizar el método intersection() es la siguiente:

```python
conjunto_A.intersection(conjunto_B)
```

Ejemplo:

```python
# Ejemplo 1:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A.intersection(conjunto_B)    # {4, 5}
```

## El operador ' & '

La sintaxis para utilizar el operador & es la siguiente:

```python
conjunto_A & conjunto_B
```

Ejemplo:

```python
# Ejemplo 2:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A & conjunto_B    # {4, 5}
```

Ahora, ¿Qué sucede cuando ambos conjuntos no tienen ningún elemento en común?

```python
# Ejemplo 3

conjunto_A = {1, 2, 3}
conjunto_B = {6, 7, 8}

conjunto_A.intersection(conjunto_B)    # set()
```

Python nos retorna un conjunto vacío que es representado como: 'set()'

Finalmente:

Es importante mencionar que no importa el orden en que se colocan los conjuntos ya que el resultado será el mismo:

```python
# Ejemplo 4:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B.intersection(conjunto_A)    # {4, 5}
```

```python
# Ejemplo 5:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B & conjunto_A    # {4, 5}
```

Como se observa, al ejecutarse el método, se crea un nuevo conjunto

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.
