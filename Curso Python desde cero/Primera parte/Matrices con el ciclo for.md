# Matrices

Al trabajar con matrices, es necesario tener acceso a cada uno de sus elementos de manera automatizada, ya que de esta manera podemos manipular y trabajar con la información contenida dentro de las matrices.

Para esta situación, podemos apoyarnos del ciclo o bucle for, el cual nos permitirá automatizar el acceso a la información contenida dentro de cada fila y columna de una matriz.

Para este fin, a continuación se presentan tres formas distintas de imprimir los elementos de una matriz en Python:

\>> Imprimiendo fila a fila:

```python
# Ejemplo 1:

matriz = [[1, 2 ,3],
		  [4, 5, 6],
		  [7, 8, 9]]

for fila in matriz:
	print(fila)

# Salida:

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
```

Como se observa en el ejemplo anterior, y gracias al ciclo for, somos capaces de imprimir las filas de la matriz y lograr una impresión "limpia" en la terminal.

Pero, si lo queremos, también podemos imprimir elemento a elemento:

```python
# Ejemplo 2:

matriz = [[1, 2 ,3],
		  [4, 5, 6],
		  [7, 8, 9]]

for fila in matriz:
	for elemento in fila:
		print(elemento)

# Salida:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

Como se observa, el ciclo for anidado ayuda a imprimir uno a uno los elementos de cada fila. Lo cual es útil si se desea trabajar con dichos elementos.

Finalmente, y retomando el ejemplo 2, podemos dar un poco de formato a nuestra salida para lograr imprimir uno a uno los elementos de la matriz y darle su formato caracteristico:

```python
# Ejemplo 3:

matriz = [[1, 2 ,3],
		  [4, 5, 6],
		  [7, 8, 9]]

for fila in matriz:
	for elemento in fila:
		print(elemento, end = " ")
		
	print()

# Salida:

# 1 2 3
# 4 5 6
# 7 8 9
```

En el ejemplo 3, nos apoyamos del parámetro [end](Los%20parámetros%20end%20y%20sep.md) para lograr imprimir los elementos de manera horizontal y nos apoyamos del **print()** vacío para que las filas de nuestra matriz se impriman en líneas diferentes.

Finalmente:

 > Se recomienda practicar este tema modificando los parámetros y valores de los ejercicios anteriormente presentados para comprender su funcionamiento.