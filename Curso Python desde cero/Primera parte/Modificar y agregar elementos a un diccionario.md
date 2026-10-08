# Diccionarios

Al trabajar con diccionario podemos encontrarnos con la necesidad de realizar modificaciones a algunos de los valore contenidos dentro del mismo, o bien, agregar nuevos elementos compuestos por su clave y valor.

En Python, es posible realizar modificaciones, y a su vez, agregar nuevos elementos a nuestros diccionarios con un una sencilla sintaxis:

```python
diccionario[clave] = nuevo_valor
```

Ejemplo:

```python
# Ejemplo 1:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

print(f"Diccionario original: {diccionario}")
diccionario["a"] = 0
print(f"Diccionario despues de la modificación {diccionario}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario despues de la modificación {'a': 0, 'b': 2, 'c': 3}
```

Ahora, ¿Qué sucede cuando intento modificar una clave que no existe dentro del diccionario?:

```python
# Ejemplo 2:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

print(f"Diccionario original: {diccionario}")
diccionario["d"] = 4
print(f"Diccionario despues de la modificación {diccionario}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario despues de la modificación {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Como se observa en el ejemplo anterior, cuando no existe la clave, esta se agrega al diccionario al final de los **'items'** de nuestro diccionario.

Donde, recordemos, un **'item'** es el par **'clave, valor'** dentro de mi diccionario.

Finalmente:

> Se recomienda ejecutar el programa a continuación para observar su salida. Además, también se anima al lector a modificar los valores y agregar más elementos para crear un programa más completo.

```python
diccionario_frutas = {"manzana": 2.50,
					  "banana": 1.75,
					  "naranja": 3.00,
					  "mango": 4.25
					  }

print(f"Diccionario original: {diccionario_frutas}")

diccionario_frutas["manzana"] = 3.50
print(f"Diccionario modificado: {diccionario_frutas}")

diccionario_frutas["uva"] = 4.00
print(f"Nuevo valor agregado: {diccionario_frutas}")
```
