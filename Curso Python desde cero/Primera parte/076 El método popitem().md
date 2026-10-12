# El método popitem()

El método popitem() se utiliza para eliminar y devolver el ultimo par clave-valor agregado a un diccionario.

Este método eliminará el par clave-valor y lo devolverá como una tupla de dos elementos.

\>> El primer elemento dentro de la tupla corresponde a la clave.
\>> El segundo elemento dentro de la tupla corresponde al valor.

## Sintaxis

La sintaxis para utilizar el método popitem(), es la siguiente:

```python
# Este elemento no trabaja con ningún argumento.
nombre_diccionario.popitem()

# Sin embargo, por el comportamiento del mismo, se recomienda utilizarlo en compañia de una variable en donde almacenar el valor devuelto.

item = nombre_diccionario.popitem()
```

Ejemplo:

```python
# Ejemplo 1
dict_name = {"a": 1,
			 "b": 2,
			 "c": 3}

print(f"Diccionario original: {dict_name}")

# Eliminamos el último par de nuestro diccionario y lo almacenamos en una variable.
item = dict_name.popitem()
print(f"Diccionario: {dict_name} - Elemento eliminado: {item}")


# Eliminamos el último par de nuestro diccionario pero no lo almacenamos en una variable.
dict_name.popitem() 

print(f"Diccionario: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario: {'a': 1, 'b': 2} - Elemento eliminado: ('c', 3)
# Diccionario: {'a': 1}
```

Como se observa, el método funciona aún si no lo almacenamos en una variable. Y, si lo hacemos, el método nos devuelve el par **clave-valor** eliminado en forma de tupla donde, como se explico anteriormente, el primer elemento corresponde a la **'key'** y el segundo al elemento contenido.

Finalmente:

> Se recomienda modificar los ejemplos anteriormente presentados para mejorar la compresión del tema. Además, también se anima al lector a desarrollar sus propios programas donde se incluya este método.

