# El módulo random

El módulo random proporciona funciones para generar números pseudoaleatorios.

Podemos utilizarlo para realizar tareas como seleccionar elementos al azar, mezclar listas , generar números aleatorios, entre otras funciones.

Ejercicio:

```python
import random

# randint (), devuelve un entero aleatorio en el rango [a, b]
num = random.randint(1, 100)
print ("num = random.randint(1, 100):", num)

# random (), devuelve un número de punto flotante en el rango [0.0, 1.0]
num = random.random()
print ("num = random.random():", num)

# randrange (), devuelve un elemento aleatorio de la secuencia generada por range (start, stop, step)
num = random.randrange(0, 100, 2)
print ("num = random. randrange (0, 100, 2):", num)

# Salida:

# num = random.randint(1, 100): 79
# num = random.random(): 0.45779243747539655
# num = random. randrange (0, 100, 2): 6
```

Al ser un modulo para "aleatorizar", con cada ejecución del código las salidas cambiarán.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.

