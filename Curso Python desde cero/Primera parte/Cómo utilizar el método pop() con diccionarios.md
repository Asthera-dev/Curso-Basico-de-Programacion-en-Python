# El método pop()

Como lo hemos aprendido previamente, en Python, pop() es un método que se usa para eliminar y devolver un elementos de una lista, un conjunto o un diccionario. 

Sin embargo, cuando utilizamos el método pop() con diccionario, su comportamiento puede variar dependiendo de los argumentos que le pasemos.

Al trabajar con diccionarios, el método pop() elimina el elemento del diccionario correspondiente a la clave especificada y devuelve su valor. 

Si la clave no se encuentra en el diccionario y se proporciona un valor predeterminado, se devuelve ese valor predeterminado en lugar de generar un error.

Es importante tener en cuenta que si no se proporciona un valor predeterminado y la clave no se encuentra en el diccionario, el método pop() generará un error **KeyError.**

Por lo tanto, se recomienda usar el método pop() solo cuando se tiene certeza de que la clave existe en el diccionario o proporcionar un valor predeterminado adecuado para evitar errores.

## Sintaxis

La sintaxis para utilizar el método pop() con diccionarios, es la siguiente:

```python
dict_name.pop(key) # Trabajando con un argumento

dict_name.pop(key, value) # Trabajando con dos argumentos
```

Donde:
* **key**: Es la clave que deseamos eliminar de nuestro diccionario.
* **value**: Es el valor que pop nos retornará en caso de que la clave **NO** exista.

Ejemplos:

```python
# Ejemplo 1 (Trabajando con un argumento):

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

valor_eliminado = dict_name.pop("a")
print(f"Valor eliminado: {valor_eliminado} | Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Valor eliminado: 1 | Diccionario modificado: {'b': 2, 'c': 3}
```

Como se observa, el método pop() nos devuelve el valor de la clave especificada y, además, el par **clave-valor** especificado es eliminado de nuestro diccionario.

```python
# Ejemplo 2 (Trabajando con un argumento):

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(dict_name.pop("z"))    # Salida: KeyError: 'z'
```

Ahora, como se nota en el ejemplo 2, cuando solo especificamos un argumento y dicha clave no existe en el diccionario, pop() nos marca un error de llave donde nos anuncia que la clave a buscar no existe dentro de nuestro diccionario. 

Para evitar este error, solo es necesario añadir el segundo argumento dentro de pop() o especificar una clave que si exista:

```python
# Ejemplo 3 (Trabajando con ambos argumentos):

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

valor_eliminado = dict_name.pop("z", "No se encuentra la clave.")
print(f"Valor eliminado: {valor_eliminado} | Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Valor eliminado: No se encuentra la clave. | Diccionario modificado: {'a': 1, 'b': 2, 'c': 3}
```

Como se observa, al añadir el segundo argumento; que puede ser un String o un dato numérico, el método pop() retorna dicho valor si la clave no existe dentro de nuestro diccionario. Evitando de esta forma errores al ejecutar nuestro código y teniendo un mejor control del mismo.

Finalmente:

> Se recomienda modificar los ejemplos anteriormente presentados para mejorar la compresión del tema. Además, también se anima al lector a desarrollar sus propios programas donde se incluya este método.