# Diccionarios

Al trabajar con diccionarios, podemos acceder a la información contenida dentro de ellos a través de la clave que hace referencia a cada uno de sus elementos.

La sintaxis para acceder a los elementos  de un diccionarios es la siguiente:

```python
nombre_diccionario[key]
```

Veamos algunos ejemplos:

```python
# Ejemplo 1:
diccionario = {"a": 1,
			   "e": 2
			   }

print(diccionario["a"])    # Salida: 1
print(diccionario["e"])    # Salida: 2
```

```python
# Ejemplo 2:
diccionario = {"numeros": [18, 20, 28],
			   "grupo": {"a": 1, "b": 2}
			   }

print(diccionario["numeros"])    # Salida: [18, 20, 28]
print(diccionario["grupo"])    # Salida: {'a': 1, 'b': 2}
```

Como observamos en el ejemplo 2, con esta sintaxis podemos consultar la totalidad de lo que contenga nuestra clave. Es decir, al imprimir se mostrarían las listas y diccionarios contenidos en su totalidad. Ahora, ¿Y si queremos acceder a los elementos de estos diccionarios o listas internos?

```python
# Ejemplo 3:
diccionario = {"numeros": [18, 20, 28],
			   "grupo": {"a": 1, "b": 2}
			   }

# Imaginemos que deseamos obtener el número 20 de la lista
print(diccionario["numeros"][1])    # Salida: 20

# Ahora deseamos obtener el valor de la clave 'b' del diccionario interno
print(diccionario["grupo"]["b"])    # Salida: 2
```

Como se observa, primero tenemos que hacer referencia a la llave que contiene la lista o diccionario (**'numeros' o 'grupo'**) y, posteriormente, indicar la posición del elementos; en el caso de las listas (**0 , 1 , 2 , ...**), o la clave; en el caso de los diccionarios (**key**).

Ahora, ¿Qué sucede si tratamos de buscar una clave (**key**) que no existe dentro de nuestro diccionario?:

```python
# Ejemplo 4:
diccionario = {"a": 1,
			   "e": 2
			   }

print(diccionario["z"])    # Salida: KeyError: 'z'
```

Como se observa, Python nos lanza un error donde se nos indica que la llave a buscar no existe. La solución sería verificar la llave o agregar la clave inexistente.

Finalmente:

 > Se recomienda practicar este tema modificando los parámetros y valores de los ejercicios anteriormente presentados para comprender su funcionamiento.

