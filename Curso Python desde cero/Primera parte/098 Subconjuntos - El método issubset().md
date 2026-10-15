# Subconjuntos

Un subconjunto es un conjunto que contiene solo elementos que también están presentes en otro conjunto más grande. 

Al tener dos conjuntos llamados  A y B, se dice que B es un subconjunto de A si cada elemento de B también esta presente en A. Es decir, si todos los elementos de B forman parte de A, B es un subconjunto de A.

Veamos algunos ejemplos para comprenderlo mejor: 

```python
# Ejemplo 1: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 4}

# ¿El Conjunto B es subconjunto de A?
# True

conjunto_b.issubset(conjunto_a)    # True
```

Como se observa, el conjunto B es un subconjunto de A debido a que todos sus elementos también están contenidos en A.

```python
# Ejemplo 2: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 8}

# ¿El Conjunto B es subconjunto de A?
# False

conjunto_b.issubset(conjunto_a)    # False
```

Como el elementos '8' no esta contenido dentro del conjunto A, podemos concluir que el conjunto B no es un subconjunto de A.

Es importante siempre colocar el subconjunto a la izquierda y el conjunto dentro de los paréntesis:

```python
# Ejemplo 3: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 4}

# ¿El Conjunto A es subconjunto de B?
# False

conjunto_a.issubset(conjunto_b)    # False 
```

Como se nota, al cambiar las posiciones de los conjuntos, la salida también cambia ya que aunque ambos conjuntos comparten elementos, el conjunto A no es subconjunto de B por tener más elementos.

___

En Python, para comprobar si un conjunto B es subconjunto de un conjunto A, podemos utilizar el método issubset(), o bien, utilizar los operadores de comparación **<=** y **<**.

## El método issubset()

El método issubset() se utiliza para comprobar si un conjunto dado es un subconjunto de otro conjunto.

Este método devolverá True si el conjunto en el que se llama al método es un subconjunto del conjunto anterior como argumento, y devolverá False en caso contrario.

### Sintaxis:

La sintaxis para utilizar el método issubset() es la siguiente:

```python
conjunto_b.issubset(conjunto_a)
```

## Operadores de subconjunto

Los operadores **<=** y **<**, que cuando trabajamos con conjuntos son mejor conocidos como operadores de subconjunto, se utilizan para comparar conjuntos y determinar si un conjunto es un subconjunto inclusivo o si es un subconjunto estricto.

### Subconjunto inclusivo (<=)

El operador <= se utiliza para comprobar si un conjunto es un subconjunto inclusivo de otro conjunto. 

Este operador devuelve True si el conjunto a la izquierda del operador es un subconjunto del conjunto a la derecha, lo que significa que contiene todos los elementos de ese conjunto.

Además, si ambos conjuntos son iguales, el operador <= también devolverá True.

Ejemplos:

```python
# Ejemplo 4:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 4}

conjunto_b <= conjunto_a    # True
```

```python
# Ejemplo 5:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {-1, 0}

conjunto_b <= conjunto_a    # False
```

```python
# Ejemplo 6:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 2, 3, 4 ,5}

conjunto_b <= conjunto_a    # True
```

### Subconjunto estricto (<)

El operador < se utiliza para comprobar si un conjunto es un subconjunto estricto de otro conjunto.

Este operador devuelve True si el conjunto a la izquierda del operador es un subconjunto del conjunto a la derecha, pero no son iguales. En otras palabras, el conjunto de la izquierda contiene algunos de los elementos del conjunto de la derecha.

Además, si ambos conjuntos son iguales, el operador < devolverá False.

Ejemplos: 

```python
# Ejemplo 7:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 4}

conjunto_b < conjunto_a    # True
```

```python
# Ejemplo 8:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {6, 0}

conjunto_b < conjunto_a    # False
```

```python
# Ejemplo 9:

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 2, 3, 4 ,5}

conjunto_b < conjunto_a    # False
```

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.
