# El método update()

El método update() se utiliza para actualizar o agregar elementos a un diccionario. Este método acepta un diccionario como argumento, y luego agrega o actualiza los elementos en el diccionario original.

Es importante tener en cuenta, que al utilizar el método update() para agregar elementos a un diccionario, se deben de tomar ciertas precauciones ya que podríamos sobrescribir valores existentes y, por consecuencia, perder información.

## Sintaxis

La sintaxis para utilizar el método update(), es la siguiente:

```python
dict_name.update(diccionario)
```

Ejemplos:

```python
# Ejemplo 1:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

dict_name.update({"z": 4})

print(f"Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario modificado: {'a': 1, 'b': 2, 'c': 3, 'z': 4}
```

Como se observa, este método agrego el argumento **clave-valor** a mi diccionario original sin modificar los ítems ya existentes.

```python
# Ejemplo 2:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

dict_name.update({"z": 4, "d": 5})

print(f"Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario modificado: {'a': 1, 'b': 2, 'c': 3, 'z': 4, 'd': 5}
```

Además, este método permite agregar varios ítems.

Ahora, ¿Qué sucede cuando colocamos una clave que ya existe?

```python
# Ejemplo 3:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

dict_name.update({"a": 6})

print(f"Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario modificado: {'a': 6, 'b': 2, 'c': 3}
```

Como se observa, el valor para la clave 'a' fue actualizado por el método. Esto, además, también se puede aplicar para varias claves simultáneamente.

```python
# Ejemplo 4:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Diccionario original: {dict_name}")

dict_name.update({"a": 6, "b": 5})

print(f"Diccionario modificado: {dict_name}")

# Salida:

# Diccionario original: {'a': 1, 'b': 2, 'c': 3}
# Diccionario modificado: {'a': 6, 'b': 5, 'c': 3}
```

Finalmente:

> Se recomienda utilizar este método en conjunto con todas las notas anteriores para empezar a realizar sus propios programas.