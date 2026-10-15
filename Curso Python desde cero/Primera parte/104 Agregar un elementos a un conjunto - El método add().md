# El método add()

El método add() se utiliza para agregar un solo elemento a un conjunto.

Si el elemento ya existe en el conjunto, el método no realizara ninguna acción ya que los conjuntos no permiten elementos duplicados.

Este método es útil cuando se desea agregar un único elemento a un conjunto, por tal motivo, este método solo permite trabajar con un argumento de manera simultánea.

## Sintaxis

La sintaxis para utilizar el método add() es la siguiente:

```python
# Importante recordar que este método trabaja con un solo argumento.

nombre_conjunto.add(elemento)
```

Ejemplos:

```python
# Ejemplo 1:

frutas = {"manzana", "pera", "uva"}

print(f"Conjunto antes del cambio {frutas}")

frutas.add("naranja")

print(f"Conjunto depués del cambio {frutas}")

# Salida:

# Conjunto antes del cambio {'uva', 'pera', 'manzana'}
# Conjunto depués del cambio {'uva', 'naranja', 'pera', 'manzana'}
```

Como se observa, el elemento se agrega de manera correcta a nuestro conjunto.

```python
# Ejemplo 2:

frutas = {"manzana", "pera", "uva"}

print(f"Conjunto antes del cambio {frutas}")

frutas.add("pera")

print(f"Conjunto depués del cambio {frutas}")

# Salida:

# Conjunto antes del cambio {'uva', 'pera', 'manzana'}
# Conjunto depués del cambio {'uva', 'pera', 'manzana'}
```

Al ya existir el elemento 'pera' dentro del conjunto, nuestro método no agrega el elemento de nuevo y, por lo tanto, nuestro conjunto no cambia. 

Finalmente:

> Esta nota es corta debido a la simpleza de este método.
> Se recomienda al lector practicar incluyendo este método a sus programas.