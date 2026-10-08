# Diccionarios

Como lo hemos aprendido previamente, al trabajar con diccionario podemos acceder a cada uno de sus elementos de manera rápida y eficiente a través de su clave correspondiente. 

Sin embargo, existe la posibilidad de desconocer las claves y, por consecuencia, los elementos que conforman nuestros diccionarios.

Afortunadamente, contamos con tres métodos de gran utilizad, los cuales son: **items()**, **[keys()](Primera%20parte/El%20método%20keys().md)** y **[values()](Primera%20parte/EL%20método%20values().md)**.

## Los métodos items(), keys() & values()

Estos tres métodos nos permiten acceder a diferentes partes del diccionario y trabajar con ellas de manera independiente.

## El método items()

El método items() se utiliza para obtener una lista de tuplas que contienen tanto la clave como el valor de cada elemento del diccionario. Es decir, este método devuelve todos los elementos del diccionario como una lista de tuplas.

### Sintaxis

La sintaxis para utilizar el método items(), es la siguiente:

```python
nombre_diccionario.items()
```

Ejemplo:

```python
# Ejemplo 1:
 
diccionario = {"a": 1, # Item
			   "b": 2, # Item
			   "c": 3  # Item
			   }

diccionario.items()    # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)])
```

Donde un **'item'** es el conjunto de una clave con su valor. En el ejemplo anterior, tenemos tres **'items'**.

Igualmente, como se puede notar, la salida viene acompañada de la frase **'dict_items()'** y, en su interior, esta la lista de tuplas: **\[ ('a', 1), ('b', 2), ('c', 3) ]**

Si queremos trabajar con los elementos generados por este método, tendríamos que convertir nuestra salida con ayuda del **'[constructor list()](Primera%20parte/Constructor%20list()%20-%20Convertir%20objetos%20a%20listas.md)'**:

```python
# Ejemplo 2:
 
diccionario = {"a": 1, # Item
			   "b": 2, # Item
			   "c": 3  # Item
			   }

list(diccionario.items())    # Salida: [('a', 1), ('b', 2), ('c', 3)]
```

De esta forma ya podemos acceder a las tuplas contenidas dentro de la lista con ayuda de los índices.

Finalmente:

 > Se recomienda practicar este tema en conjunto con bucles y otros métodos para observar su comportamiento y profundizar de manera autodidacta en el tema.