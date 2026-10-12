# Tuplas

Las tuplas son estructuras de datos similares a las listas que se utilizan para almacenar conjuntos de elementos de manera ordenada, y a su vez, estos elementos pueden o no estar relacionados entre sí, es decir, una tupla puede ser homogénea o heterogénea.

A diferencia de las listas, las tuplas tienen la característica de ser **inmutables**, es decir, que una vez creada la tupla su contenido no se puede modificar.

## Sintaxis

La sintaxis para crear una tupla es la siguiente:

```python
nombre_tupla = () # De esta manera se crea una tupla vacia
nombre_tupla = (elemento,) # De esta manera se crea una tupla de un elemento
nombre_tupla = (elemento, elemento, ...) # De esta manera se crea una tupla de varios elementos
nombre_tupla = elemento, elemento, ... # Tambien es posible crear una tupla sin los parentesis, pero, por buenas practicas, se recomienda colocarlos.
```

Algo interesante a mencionar sobre las tuplas en Python es que, aunque pueden contener un solo elemento, es obligatorio incluir una coma después del valor para que el interprete distinga que es una tupla y no una expresión entre paréntesis.

Ejemplo:

```python
# Ejemplo 1:

elemento = "a"

tupla_un_elemento = (elemento)

print(f"Longitud: {len(tupla_un_elemento)}\nTipo: {type(tupla_un_elemento)}")

# Salida:

# Longitud: 1
# Tipo: <class 'str'>
```

Como se observa en el ejemplo anterior, Python identifica la variable mediante **type()** como un **'str'** y no como una **tupla**. Y la longitud corresponde a la del string, no a la de la tupla.

Probemos ahora con un entero para ver el comportamiento:

```python
# Ejemplo 2:

elemento = 2

tupla_un_elemento = (elemento)

print(f"Longitud: {len(tupla_un_elemento)}\nTipo: {type(tupla_un_elemento)}")

# Salida:

# TypeError: object of type 'int' has no len()
```

Ahora Python nos devuelve un error. Esto ocurre porque, una vez más, no estamos creando una tupla. 
En el ejemplo anterior, colocamos un número entero entre paréntesis y Python lo interpreta como tal. Y, como un número entero no tiene el método **len()**, nos lanza el error.

Ahora veamos la forma correcta de crear una tupla de un elemento:

```python
# Ejemplo 3:

elemento = 2

tupla_un_elemento = (elemento, ) # Añadimos una coma al final

print(f"Longitud: {len(tupla_un_elemento)}\nTipo: {type(tupla_un_elemento)}")

# Salida:

# Longitud: 1
# Tipo: <class 'tuple'>
```

Como se observa, ahora Python ya no nos muestra el error anterior debido a que, al agregar la coma al final, nuestra variable deja de ser una expresión y pasa a ser una tupla.

Ahora veamos el ejemplo donde trabajamos sin paréntesis:

```python
# Ejemplo 4:

elemento = "a"

tupla_un_elemento = elemento, # Trabajamos sin parentesis, solo agregamos la coma y, en su defecto, más elementos.

print(f"Longitud: {len(tupla_un_elemento)}\nTipo: {type(tupla_un_elemento)}")

# Salida:

# Longitud: 1
# Tipo: <class 'tuple'>
```

___

### Más ejemplos de tuplas:

#### Tupla homogénea: 

```python
# Tupla homogénea (Contiene elementos del mismo tipo de dato):

nombre_tupla = (3, 2)

print(nombre_tupla)    # Salida: (3, 2)
```

#### Tupla heterogénea:

```python
# Tupla heterogénea (Contiene elementos de diferente tipo de dato):

nombre_tupla = (3, True, "Hola", 2.5)

print(nombre_tupla)    # Salida: (3, True, 'Hola', 2.5)
```

#### Tupla con otro tipo de estructura de datos en su interior:

```python
# Tupla con estructuras de datos en su interior (listas, diccionarios, tuplas, etc.):

nombre_tupla = ([1, 2, 3], {"uno": 1, "dos": 2}, (3,2))

print(nombre_tupla)    # Salida: ([1, 2, 3], {'uno': 1, 'dos': 2}, (3, 2))
```

Algo que trataremos en la siguiente nota es que nosotros podemos modificar los datos dentro de los diccionarios y listas contenidas en la tupla.

#### Tupla de un solo elemento:

```python
# Tupla con un solo elemento en su interior:

nombre_tupla = (2, )

print(nombre_tupla)    # Salida: (2,)
```

#### Tuplas son paréntesis:

```python
# Declarando una tupla sin colocar paréntesis:

nombre_tupla = 3, True, "Hola", 2.5

print(nombre_tupla)    # Salida: (3, True, 'Hola', 2.5)
```

Finalmente:

> Se anima al lector a incluir las tuplas en sus códigos y proyectos. Además, se recomienda modificar los ejercicios anteriores para observar el comportamiento de esta estructura de datos en diferentes situaciones.

