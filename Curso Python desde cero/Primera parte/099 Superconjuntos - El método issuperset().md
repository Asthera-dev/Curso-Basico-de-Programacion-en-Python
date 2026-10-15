# Superconjuntos

Un superconjunto, también conocido como superset, se refiere a un conjunto que contiene todos los elementos de otro conjunto. 

En Python, para comprobar si un conjunto es el supercojunto de otro conjunto podemos utilizar el método issuperset(), o bien, los operadores de superconjunto >= y >.

## El método issuperset()

La sintaxis para utilizar el método issuperset(), es la siguiente: 

```python
conjunto_a.isspuerset(conjunto_b)
```

Ejemplos:

```python
# Ejemplo 1: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 4}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a.issuperset(conjunto_b)    # True
```

```python
# Ejemplo 2: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {0, 8}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a.issuperset(conjunto_b)    # False
```

```python
# Ejemplo 3: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 2, 3, 4 ,5}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a.issuperset(conjunto_b)    # True
```

## Operadores de superconjunto

La sintaxis para utilizar los operadores **>=** y **>** es la siguiente:

```python
conjunto_a >= conjunto_b
conjunto_a > conjunto_b
```

### Superconjunto inclusivo >=

Ejemplos:

```python
# Ejemplo 1: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {2, 5}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a >= conjunto_b    # True
```

```python
# Ejemplo 2: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {0, 5}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a >= conjunto_b    # False
```

```python
# Ejemplo 3: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 2, 3, 4 ,5}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a >= conjunto_b    # True
```

### Superconjunto estricto >

Ejemplos:

```python
# Ejemplo 1: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 4}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a > conjunto_b    # True
```

```python
# Ejemplo 2: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {-3, 7}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a > conjunto_b    # False
```

```python
# Ejemplo 3: 

conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {1, 2, 3, 4 ,5}

# ¿El Conjunto a es un superconjunto de B?

conjunto_a > conjunto_b    # False
```

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.

