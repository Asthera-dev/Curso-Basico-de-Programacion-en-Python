# El método keys()

Este método se utiliza para obtener una lista de todas las claves del diccionario. Es decir, este método devuelve las claves del diccionario como una lista.

# Sintaxis:

La sintaxis para utilizar el método keys() es la siguiente:

```python
nombre_diccionario.keys()
```

Ejemplos:

```python
# Ejemplo 1:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

diccionario.keys()    # Salida: dict_keys(['a', 'b', 'c'])
```

Como se observa, este método nos devuelve una lista con todas las claves de nuestro diccionario y, al igual que con el método items(), no podemos trabajar con dicha lista hasta convertirla en una lista.

```python
# Ejemplo 2:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

list(diccionario.keys())    # Salida: ['a', 'b', 'c']
```

De esta forma ya podemos acceder a las claves contenidas dentro de la lista con ayuda de los índices.

Finalmente:

 > Se recomienda practicar este tema en conjunto con bucles y otros métodos para observar su comportamiento y profundizar de manera autodidacta en el tema.