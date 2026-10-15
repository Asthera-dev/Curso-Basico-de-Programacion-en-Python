# Diferencia Simétrica

La diferencia simétrica entre dos conjuntos, llamados A y B, se refiere a la operación que devuelve un conjunto que contiene todos los elementos que están en A pero no en B, así como todos los elementos que están en B pero no en A.

Es decir, la diferencia simétrica devuelve un conjunto que contiene todos los elementos exclusivos de ambos conjuntos.

Si ambos conjuntos tienen elementos en común, estos elementos no serán incluidos en el resultado de la diferencia simétrica.

En Python existen dos alternativas para realizar la diferencia simétrica entre dos conjuntos.

Utilizando el método **symmetric_difference()**, o bien, el operador **" ^ "**.

## symmetric_difference()

La sintaxis para utilizar el método symmetric_difference() es la siguiente:

```python
conjunto_A.symmetric_difference(conjunto_B)
```

Ejemplos:

```python
# Ejemplo 1:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A.symmetric_difference(conjunto_B)    # {1, 2, 3, 6, 7, 8}
```

Como se observa, el nuevo conjunto generado contiene a los elementos exclusivos de cada conjunto. Además, en este método el orden de los conjuntos no importa:

```python
# Ejemplo 2:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B.symmetric_difference(conjunto_A)    # {1, 2, 3, 6, 7, 8}
```
## El operador " ^ "

La sintaxis para utilizar el operador " ^ " es la siguiente:

```python
conjunto_A ^ conjunto_B
```

Ejemplos:

```python
# Ejemplo 3:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_A ^ conjunto_B    # {1, 2, 3, 6, 7, 8}
```

```python
# Ejemplo 4:

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

conjunto_B ^ conjunto_A    # {1, 2, 3, 6, 7, 8}
```

Como se observa, el resultado es el mismo sin importar si utilizo simmetric_difference() o el símbolo ' ^ '.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.