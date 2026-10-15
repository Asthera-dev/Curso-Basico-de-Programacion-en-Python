# Unión de conjuntos

La unión entre conjuntos es una operación que combina dos conjuntos en uno solo, manteniendo únicamente los elementos únicos de ambos conjuntos.

En Python, existen dos alternativas con las cuales podemos realizar la unión de dos conjuntos. Utilizando el método **union()** o bien, el operador **' | '**.

## Método union()

La sintaxis para utilizar el método union() es la siguiente:

```python
conjunto_A.union(conjunto_B)
```

Ejemplo:

```python
# Ejemplo 1:

conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

conjunto_A.union(conjunto_B)    # {1, 2, 3, 4, 5}
```

Como aprendimos en notas anteriores, los conjuntos tienen elementos únicos. Por lo cual, a pesar de que ambos conjuntos tienen e número 3, al unirlos este solo aparecerá una vez.
## El operador ' | '

La sintaxis para utilizar el operador ' | ' es la siguiente:

```python
conjunto_A | conjunto_B
```

Ejemplo:

```python
# Ejemplo 2:

conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

conjunto_A | conjunto_B    # {1, 2, 3, 4, 5}
```


Finalmente:

Es importante mencionar que no importa el orden en que se colocan los conjuntos ya que el resultado será el mismo:

```python
# Ejemplo 3:

conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

conjunto_B.union(conjunto_A)    # {1, 2, 3, 4, 5}
```

```python
# Ejemplo 4:

conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

conjunto_B | conjunto_A    # {1, 2, 3, 4, 5}
```

Como se observa, al ejecutarse el método, se crea un nuevo conjunto

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.
