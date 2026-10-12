# La clase range

En Python, la clase range, genera secuencias de números inmutables, es decir, que no se pueden modificar, estas secuencias se generan a partir de un rango previamente establecido.

Generalmente la clase range, se utiliza como objeto iterable dentro de la sintaxis del ciclo o bucle for, con el cual se logran realizar las respectivas iteraciones.

La clase range nos permite trabajar con un mínimo de un argumento y un máximo de tres argumentos de manera simultánea.

Así, podremos decidir el número con el que comenzará y terminará la secuencia de números, y a su vez, indicar el incremento o decremento entre un número y el siguiente.

## Sintaxis

La sintaxis para utilizar la clase range es la siguiente:

```python
# Con un argumento:
range(stop)

# Con dos argumentos:
range(start, stop)

# Con tres argumentos:
range(start, stop, step)
```

Donde:
* **Stop**: Es un valor entero, que indica el número hasta el cual se va a generar la secuencia de números, y este número jamás formará parte de la secuencia.
* **Start**: Es un valor entero, que indica el número a partir del cual se comenzará a generar la secuencia de números, y este número siempre formará parte de la secuencia.
* **Step**: Es un valor entero, que indica el incremento o decremento de la sucesión numérica entre un número y el siguiente.

___
## Comportamiento de la clase range

### Trabajando con un solo argumento:

Al tener, por ejemplo, range(10):

\>> Python genera una secuencia consecutiva de números empezando desde cero y deteniéndose cuando esta clase adquiere el valor especificado (diez en este ejemplo). Siempre con un salto de uno.

\>> Es importante mencionar que estos números se generan "bajo demanda". Es decir, no se guardan en memoria como una variable o lista de números.

\>> La salida esperada al ejecutar este ejemplo sería una secuencia de números desde el cero hasta el nueve.

Ejemplo con el ciclo for:

```python
# Ejemplo 1:
for i in range(10):
	print(i)

# Salida:

# 0
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

Como se observa en el ejemplo anterior, la secuencia de números comienza en cero y termina hasta el número nueve (un número 'anterior' al especificado).

```python
# Ejemplo 2:
for i in range(9):
	print(i)

# Salida:

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# Ejemplo 3:
for i in range(11):
	print(i)

# Salida:

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

### Trabajando con dos argumentos

Al tener, por ejemplo, range(5, 10):

\>> Python genera una secuencia consecutiva de números empezando desde el primer argumento (cinco en este ejemplo) y deteniéndose cuando esta clase adquiere el valor especificado en el segundo (diez en este ejemplo). Siempre con un salto de uno.

\>> Al igual que en el caso anterior, estos números se generan "bajo demanda". Es decir, no se guardan en memoria como una variable o lista de números.

\>> La salida esperada al ejecutar este ejemplo sería una secuencia de números desde el cinco hasta el nueve.

Ejemplo con el ciclo for:

```python
# Ejemplo 1:
for i in range(5, 10):
	print(i)

# Salida:

# 5
# 6
# 7
# 8
# 9
```

Como se observa en el ejemplo anterior, la secuencia de números comienza desde cinco y termina hasta el número nueve (un número 'anterior' al especificado).

```python
# Ejemplo 2:
for i in range(0, 5):
	print(i)

# Salida:

# 0
# 1
# 2
# 3
# 4

# Ejemplo 3:
for i in range(10, 15):
	print(i)

# Salida:

# 10
# 11
# 12
# 13
# 14
```

### Trabajando con tres argumentos

Al tener, por ejemplo, range(0, 11, 2):

\>> Python genera una secuencia consecutiva de números empezando desde el primer argumento (cero en este ejemplo) y deteniéndose cuando esta clase adquiere el valor especificado en el segundo (once en este ejemplo). En este caso, con **un salto de dos** especificado en el tercer argumento.

\>> Al igual que en el caso anterior, estos números se generan "bajo demanda". Es decir, no se guardan en memoria como una variable o lista de números.

\>> La salida esperada al ejecutar este ejemplo sería una secuencia de números desde el cero hasta el diez con un salto de dos en dos.

Ejemplo con el ciclo for:

```python
# Ejemplo 1:
for i in range(0, 11, 2):
	print(i)

# Salida:

# 0
# 2
# 4
# 6
# 8
# 10
```

Como se observa en el ejemplo anterior, la secuencia de números comienza desde cero, avanza de dos en dos y termina hasta el número diez (un número 'anterior' al especificado).

```python
# Ejemplo 2:
for i in range(0, 11, 3):
	print(i)

# Salida:

# 0
# 3
# 6
# 9

# Ejemplo 3:
for i in range(0, 12, 4):
	print(i)

# Salida:

# 0
# 4
# 8

# Ejemplo 4:
for i in range(0, 13, 4):
	print(i)

# Salida:

# 0
# 4
# 8
# 12
```

### Trabajando con range para generar una secuencia de números en decremento

Si queremos construir una secuencia de números en decremento debemos especificar el inicio, el final y un salto de menos uno:

```python
# Forma correcta: 
for i in range(10, -1, -1):
	print(i)

# Salida:

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
```

Si no especificamos los saltos de menos uno, la clase range no nos devolverá nada:

```python
# Forma incorrecta: 
for i in range(10, -1):
	print(i)

# No genera salida porque no hay ningun elemento para recorrer.
```


>En la siguiente nota, aprenderemos a trabajar con la clase range en conjunto con el ciclo for.

