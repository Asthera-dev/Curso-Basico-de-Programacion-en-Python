# Concatenación en Python 3

Es importantes mencionar que la concatenación puede llevarse a cabo uniendo dos cadenas de caracteres, o bien, enlazando un único carácter a otra cadena de caracteres.

Hasta este punto ya hemos aprendido a concatenar Strings con Strings, y también, Strings con valores int, con ayuda del operador +.

```python
# Ejemplos de concatenaciones ya usadas:


# Concatenación de String con String
nombre = "Isai"
print("Hola" + nombre)

# Salida: Hola Ernesto


# Concatenación de String con valor int
num_uno = 5
num_dos = 4
resultado = num_uno * num_dos
print("El resultado es " + str(resultado))

# Salida: El resultado es 20
```

Además, hemos aprendido a separar elementos dentro de la función print() para imprimirlos en pantalla con ayuda de una **,**.

```python
# Ejemplo de concatenación con ayuda de la coma

nombre = "Isai"
edad = 22
print("Hola", nombre, "tienes", edad, "años")

# Salida: Hola Isai tienes 22 años

# Solo como recordatorio, al separar los elementos con coma, estas agregan automaticamente espacios en blanco en la impresión.
```

Sin embargo, existen más alternativas para concatenar en el lenguaje de programación Python, independientes a las que hemos visto hasta ahora.

Una de estas alternativas, es utilizar el método format()

El método format(), nos permite mostrar los valores contenidos en una variable y utilizarlos dentro de una cadena de caracteres, sustituyendo el nombre de la variable con un juego de {}, ubicándolas en la posición donde queremos que se muestren dichos valores.

Algo importante de mencionar, es que cuando utilizamos el método format(), la concatenación se puede realizar, sin importar que las variables sean de tipo String o de tipo numérico.

Las alternativas de sintaxis para utilizar el método format() son las siguientes:

## Alternativa de Sintaxis #1

```python
# La sintaxis es la siguiente:

# Ejemplo de cadena que queremos imprimir:
"Hola Isai tienes 22 años"

# El metodo format() nos ayuda a poder insertar las variables dentro de una cadena de carateres y poder escribir:

"Hola {} tienes {} años".format(nombre, edad)

# Y evitarnos escribir:

"Hola " + nombre + " tienes " + str(edad) + " años"

# O tambien:

"Hola", nombre, "tienes", edad, "años"
```

Donde, con el método format(), remplazamos las variables a insertar dentro de nuestro texto con un par de llaves: {}

Es importante mencionar que el método debe ir junto al texto:
```python
# Uso correcto:
"Hola {} tienes {} años".format(nombre, edad)

# Uso incorrecto (Nos arrojará un error):
"Hola {} tienes {} años" .format(nombre, edad)

# O (Igualmente, nos arrojará un error):
"Hola {} tienes {} años". format(nombre, edad)
```

Además, el orden de las variables dentro del método format() corresponde al orden en que se imprimirán las variables dentro del texto.

```python

# Ejemplo 1 de impresion:
nombre = "Isai"
edad = 22
print("Hola {} tienes {} años".format(nombre, edad))

# Salida: Hola Isai tienes 22 años

# A diferencia de la concatenación con comas que agregaban espacios en blanco automaticamente al imprimir, aqui es necesario agregar los espacios antes y despues de las llaves para que se impriman.

# Ejemplo 2 de impresion: [Con las variables (argumentos) en diferente orden dentro del metodo format]
nombre = "Isai"
edad = 22
print("Hola {} tienes {} años".format(edad, nombre))

# Salida: Hola 22 tienes Isai años
```

## Alternativa de Sintaxis #2

Las alternativas de sintaxis para utilizar el método format() son las siguientes:

```python
"Hola {nombre} tienes {edad} años".format(nombre = "Isai", edad = 22)
```

Donde las variables se inicializan dentro del método format() y, además, se escriben los nombres de las variables dentro de las llaves.

Cuando se programa de esta manera, el orden de las variables dentro del método format() deja de tomar relevancia:

```python
# Ejemplo 1 de impresion:
print("Hola {nombre} tienes {edad} años".format(nombre = "Isai", edad = 22))

# Salida: Hola Isai tienes 22 años

# Ejemplo 2 de impresion: [Con las variables dentro de las llaves en diferente orden]
print("Hola {edad} tienes {nombre} años".format(nombre = "Isai", edad = 22))

# Salida: Hola 22 tienes Isai años
```

## Alternativa de Sintaxis #3

Las alternativas de sintaxis para utilizar el método format() son las siguientes:

```python
nombre = "Isai"
edad = 22
"Hola {0} tienes {1} años".format(nombre, edad)
```

Donde las variables ya se encuentran inicializadas fuera del método format() y, dentro de las llaves, agregamos la posición de las variables dentro del método:

```python
# Ejemplo 1 de impresion:
nombre = "Isai"
edad = 22
print("Hola {0} tienes {1} años".format(nombre, edad))

# Salida: Hola Isai tienes 22 años

# Ejemplo 2 de impresion: [Con las posiciones dentro de las llaves en diferente orden]
nombre = "Isai"
edad = 22
print("Hola {1} tienes {0} años".format(nombre, edad))

# Salida: Hola 22 tienes Isai años
```

Es importante mencionar que, con este método, hay que observar la posición de nuestras variables dentro del método para lograr una correcta impresión:

```python
# Ejemplo 1 de impresion:
nombre = "Isai"
edad = 22
print("Hola {0} tienes {1} años".format(nombre, edad))

# Salida: Hola Isai tienes 22 años

# Ejemplo 2 de impresion: [Con las variables (argumentos) en diferente orden dentro del metodo format pero con la posición correcta dentro de las llaves]
nombre = "Isai"
edad = 22
print("Hola {1} tienes {0} años".format(edad, nombre))

# Salida: Hola 22 tienes Isai años
```