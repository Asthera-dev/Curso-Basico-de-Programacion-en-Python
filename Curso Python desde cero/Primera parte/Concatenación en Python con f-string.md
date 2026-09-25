# Concatenación con f-Strings

Una alternativa de concatenación más eficiente a todas las que hemos visto hasta ahora son las **literals strings** o también conocidas como ***f-Strings***

Las ***f-Strings***, fueron introducidas a partir de la versión 3.6 de Python.
Permiten agregar expresiones dentro de una constante de tipo String, y al mismo tiempo, obtener una mayor legibilidad en nuestro código.

La sintaxis para utilizar ***f-Strings*** es la siguiente:

## Sintaxis:

```python
nombre = "Isai"
edad = 22

# Uso correcto:
f"Hola {nombre} tienes {edad} años"

# Uso incorrecto:
f "Hola {nombre} tienes {edad} años"
```

Donde, antes de la cadena de texto debe ir colocada la letra ***f*** y sin espacios.

Una gran ventaja de las f-Strings es que son evaluadas al momento de su ejecución, con lo cual, es posible agregar cualquier variedad e expresiones que sean válidas. Como por ejemplo:

```python
print(f"{4+1}")

# Salida: 5
```

> A continuación, se muestran varios ejemplos el funcionamiento de las f-Strings:

```python
# Ejemplo 1:
print(f"El resultado de la suma de 4 + 1 = {4+1}")

# Salida: El resultado de la suma de 4 + 1 = 5

#############################################################################

# Ejemplo 2:
nombre = "Isai"
estatura = 1.8
edad = 22
print(f"Hola {nombre} tienes {edad} años y mides {estatura} metros.")

# Salida: Hola Isai tienes 22 años y mides 1.8 metros.

#############################################################################

# Ejemplo 3
nombre = input("¿Cual es tu nombre?: ")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un segundo número: "))

print(f"Hola {nombre} el resultado de {num_uno} + {num_dos} es: {num_uno + num_dos}")
```

