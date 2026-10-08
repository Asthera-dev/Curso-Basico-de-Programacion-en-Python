# El método get()

El método get() se utiliza para obtener los valores que están asociados a cada una de las claves de un diccionario.

El método get() es útil porque evita errores de **KeyError** al intentar obtener un valor que no existe en el diccionario.

En lugar de obtener un error, se devuelve un valor por defecto previamente establecido, o simplemente, la palabra **None**.

Además, el método get() también es más eficiente que utilizar un condicional para verificar si una clave existe en el diccionario antes de obtener su valor.

## Sintaxis

La sintaxis para utilizar el método get(), es la siguiente:

```python

diccionario_nombre.get(key) # Trabajando con un argumento

diccionario_nombre.get(key, value) # Trabajando con dos argumentos
```

Este método toma dos argumentos:

 \>> La calve (**'key'**) del valor que se desea obtener
 \>> Un valor por defecto (**'value'**), que es opcional, y se devuelve si la clave **NO** existe en el diccionario.

Ejemplos:

```python
# Ejemplo 1 (Trabajando con un solo argumento):

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3}

# Probando con claves existentes en mi diccionario:
print(dict_name.get("c")) # Salida: 3
print(dict_name.get("a")) # Salida: 1

# Probando con una clave que no existe en mi diccionario:
print(dict_name.get("z")) # Salida: None
```

Cuando trabajamos con un solo argumento este método nos devuelve sin problema los valores de las llaves existentes en mi diccionario. Y, cuando la llave no existe, me devuelve la palabra 'None' en lugar de marcarme un error que, en distribución, podría detener mi programa y arruinarlo.

```python
# Ejemplo 2 (Trabajando con ambos argumentos):

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3}

# Probando con claves existentes en mi diccionario:
print(dict_name.get("c", 4)) # Salida: 3
print(dict_name.get("a", 4)) # Salida: 1

# Probando con una clave que no existe en mi diccionario:
print(dict_name.get("z", 4)) # Salida: 4
```

Ahora, como se puede notar en el ejemplo 2, cuando trabajamos con ambos argumentos el segundo no modifica los valores que poseen nuestras claves existentes y, este segundo valor solo se muestra cuando la clave no existe, remplazando a la palabra "None".

Finalmente:

> Se recomienda ejecutar el programa a continuación para observar su salida. Además, también se anima al lector a modificar los valores y agregar más elementos para crear un programa más completo.

> Es importante mencionar la importancia de este método para ahorrar líneas de código y lograr programas mas robustos ante errores provocados por un mal ingreso de datos por parte del usuario.

```python
diccionario_frutas = {"manzana": 1.55,
					  "banana": 3.55,
					  "naranja": 1.25
					  }

print(diccionario_frutas)

precio_manzana = diccionario_frutas.get("manzana")
print(f"El precio de la manzana es: {precio_manzana}")

precio_mango = diccionario_frutas.get("mango")
print(f"El precio del mango es: {precio_mango}")

precio_mango = diccionario_frutas.get("mango", 4.55)
print(f"El precio del mango es: {precio_mango}")
```