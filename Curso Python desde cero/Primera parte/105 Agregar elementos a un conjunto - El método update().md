# El método update()

El método update() se utiliza para agregar múltiples elementos a un conjunto a la vez.

Este método puede recibir como argumento un objeto iterable, como una lista, una tupla, un diccionario, un conjunto o un String.

De esta manera, agregara todos los elementos del objeto iterable al conjunto destino. Si algún elemento ya existe en el conjunto, simplemente se omitirá.

## Sintaxis

La sintaxis para utilizar el método update() es la siguiente: 

```python
# Este método solo trabaja con un argumento

nombre_conjunto.update(objeto_iterable)
```

Ejemplo:

```python
# Ejemplo 1:

colores = {"verde", "rojo", "azul"}
nuevos_colores = ["amarillo", "morado", "azul"]

print(f"Conjunto antes del cambio {colores}")

colores.update(nuevos_colores)

print(f"Conjunto depués del cambio {colores}")

# Salida:

# Conjunto antes del cambio {'azul', 'verde', 'rojo'}
# Conjunto depués del cambio {'amarillo', 'rojo', 'verde', 'morado', 'azul'}
```

Como se observa, los colores 'amarillo' y 'morado' fueron agregados de manera exitosa al conjunto y, como el color 'azul' ya existía, se omite su adición.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.