# El método setdefault()

El método setdefault() es un método de diccionarios en Python. Este método se utiliza para asignar un valor a una clave en un diccionario si la clave no existe ya en el diccionario.

Si la clave ya existe en el diccionario, el método setdefault() simplemente devuelve el valor correspondiente a esa clave.

Si la clave no existe, el método setdefault() crea la clave con el valor especificado y devuelve ese valor.

## Sintaxis.

La sintaxis para utilizar el método setdefault() es la siguiente:

```python
# Este método nos permite trabajar con un minimo de un argumento y un maximo de dos:

dict_name.setdefault(key)    # Trabajando con un argumento

dict_name.setdefault(key, value)    # Trabajando con ambos argumentos
```

Ejemplos:

```python
# Ejemplo 1 (Trabajando con una clave existente):

dict_name = {"a": 1, 
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

print(dict_name.setdefault("a", 4))

print(f"Diccionario depués del método: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# 1
# Diccionario depués del método: {'a': 1, 'b': 2, 'c': 3}
```

Como se observa en el ejemplo 1, cuando la clave ya existe dentro de nuestro diccionario, este método nos devuelve el valor correspondiente a dicha clave y no la modifica. 

```python
# Ejemplo 2 (Trabajando con una clave inexistente):

dict_name = {"a": 1, 
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

print(dict_name.setdefault("z"))

print(f"Diccionario depués del método: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# None
# Diccionario depués del método: {'a': 1, 'b': 2, 'c': 3, 'z': None}
```

Ahora, cuando trabajamos con una clave inexistente y un argumento, este método nos retornará la palabra 'None' y, a su vez, creara un nuevo ítem dentro de nuestro diccionario donde la clave será la especificada y el valor será la palabra None.

```python
# Ejemplo 3 (Trabajando con una clave inexistente):

dict_name = {"a": 1, 
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

print(dict_name.setdefault("z", 4))

print(f"Diccionario depués del método: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# 4
# Diccionario depués del método: {'a': 1, 'b': 2, 'c': 3, 'z': 4}
```

Y, cuando trabajamos con ambos argumentos de manera simultanea y especificamos una clave inexistente, este método nos retornara el valor especificado y también crear un nuevo ítem dentro de nuestro diccionario donde la clave y el valor son los especificados como argumentos en el método setdefault()

Finalmente:

> Se recomienda ejecutar el programa a continuación para observar su salida. Además, también se anima al lector a modificar los valores y agregar más elementos para crear un programa más completo.

```python
frutas = {"manzana": 2,
		  "banana": 3,
		  "naranja": 1
		  }

print(f"{frutas} \n")

# Intentamos agregar una clave que ya existe en el diccionario
return_value = frutas.setdefault("banana", 4)
print(f"El valor retornado de ('banana', 4) es: {return_value}")
print(f"El diccionario actualizado es: {frutas} \n")

# Intentamos agregar una clave que no existe en el diccionario sin valor
return_value = frutas.setdefault("kiwi")
print(f"El valor retornado de ('kiwi) es: {return_value}")
print(f"El diccionario actualizado es: {frutas} \n")

# Intentamos agregar una clave que no existe en el diccionario con valor
return_value = frutas.setdefault("mango", 5)
print(f"El valor retornado de ('mango', 5) es: {return_value}")
print(f"El diccionario actualizado es: {frutas} \n")

```