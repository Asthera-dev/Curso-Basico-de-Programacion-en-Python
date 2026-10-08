# El método values()

Este método se utiliza para obtener una lista de todos los valores del diccionario. Es decir, este método devuelve los valores del diccionario como una lista.

## Sintaxis

La sintaxis para utilizar el método values(), es la siguiente:

```python
nombre_diccionario.values()
```

Ejemplos:

```python
# Ejemplo 1:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

diccionario.values()    # Salida: dict_values([1, 2, 3])
```

Como se observa, este método nos devuelve una lista con todos los valores de nuestro diccionario y, al igual que con el método keys(), no podemos trabajar con dicha lista hasta convertirla en una lista.

```python
# Ejemplo 2:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

list(diccionario.values())    # Salida: [1, 2, 3]
```

De esta forma ya podemos acceder a los elementos contenidos dentro de la lista con ayuda de los índices.

Finalmente:

 > Se recomienda practicar este tema en conjunto con bucles y otros métodos para observar su comportamiento y profundizar de manera autodidacta en el tema.