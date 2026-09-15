# Parámetros sep y end

La función print(), es quizás una de las herramientas más utiles en el lenguaje de programación Python, al momento de interactuar con los usuarios de nuestros programas.

Por tal motivo, es indispensable conocer la manera en que podemos manipular dichas impresiones en pantalla, con la finalidad de tener el control completo del texto a mostrar.

## Parámetro end

El parámetro end se utiliza para agregar cualquier cadena de caracteres al final de la salida e impresión en pantalla de la función print()

Además, por defecto la función pront() genera un salto de línea al terminar su ejecución, sin embargo, con ayuda del parámetro end, es posible evitar este salto de línea.

> Para comprender este parámetro, observemos el siguiente ejercicio:

```python
print("Esto es un")
print("ejemplo")

# Salida:
		# Esto es un
		# ejemplo

# Como se puede observar, la función print() genera un salto de linea.
#############################################

# En cambio, cuando usamos print() con el parámetro en, podemos "eliminar" el salto de linea y, ademas, podemos agregar algun elemento en su lugar.

# Ejemplo:
print("Esto es un", end="")
print("ejemplo")

# Salida:
		# Esto es unejemplo

# Observamos que el salto de linea ha desaparecido, sin embargo, tambien podemos agregar otro elemento enmedio en forma de str.

# Ejemplo:
print("Esto es un", end=" ")
print("ejemplo")

# Salida:
		# Esto es un ejemplo

# Observamos que al agregar un espacio en blanco dentro del parametro, este se agrego en nuestra salida. Esto funciona con cualquier otro elemento.

# Ejemplo:
print("Esto es un", end="*+-")
print("ejemplo")

# Salida:
		# Esto es un*+-ejemplo
```

# Parámetro sep

En ocasiones, es posible que deseemos imprimir múltiples valores de manera legible utilizando la función print().

El parámetro sep, se utiliza para dar formato a las cadenas de caracteres que deben imprimirse en pantalla, agregando un separador entre las cadenas que se imprimirán.

> Para comprender este parámetro, observemos el siguiente ejercicio:

```python
print("1","2","3","4","5")

# Salida: 1 2 3 4 5

# Al imprimir varios stings separados por comas, la salida nos muestra estos strings separados unicamente por espacios generados automaticamente. Sin embargo, si queremos eliminarlos, solo debemmos agregar el parámetro sep

print("1","2","3","4","5", sep="")

# Salida: 12345

# Y, al igual que con end, podemos agregar strings si escibimos dentro de las comillas del parámetro.

print("1","2","3","4","5", sep=", ")

# Salida: 1, 2, 3, 4, 5
```

