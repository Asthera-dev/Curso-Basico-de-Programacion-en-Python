# Los métodos strip(), rstrip() y lstrip()

En Python, al trabajar con cadenas de caracteres, en ocasiones surge la necesidad de eliminar espacios en blanco o algún carácter en específico, ya sea al inicio o bien, al final de la cadena.

Para apoyarnos ante esta situación, en Python contamos con tres métodos de gran utilidad.

Los cuales son strip(), rstrip() y lstrip()

## El método strip()

El método strip() se utiliza para eliminar caracteres especificados al inicio y al final de una cadena de caracteres, tomando en cuenta que si a el método strip() no se le especifica uno o más caracteres a eliminar, solo eliminara espacios en blanco y saltos de línea.

Es importante mencionar que el método stip() solo puede eliminar los caracteres al inicio y al final de la cadena, y no los caracteres que se encuentren en la parte central.

### Sintaxis:
La sintaxis para utilizar el método strip() es la siguiente:

```python
# Sintaxis básica del método
cadena.strip()

# Ejemplo 1:
cadena = " Hola Ernesto "
cadena = cadena.strip()

print(cadena)

# Salida: Hola Ernesto
# (Elimina los espacios en blanco del inicio y final)
```

Cabe destacar que este método también diferencia mayusculas de minusculas:

``` python
# Ejemplo 2:
cadena = "Hola Ernesto"
cadena = cadena.strip("O")
print(cadena)

# Salida: Hola Ernesto
# No se elimina ningún caracter debido a qu eno existe una 'O' al inicio o final

# Ejemplo 3:
cadena = "Hola Ernesto"
cadena = cadena.strip("o")
print(cadena)

# Salida: Hola Ernest
# Se elimina el caracter 'o' del final
```

 La forma en que opera este método cuando se especifican más de un carácter dentro del parámetro stip() es:

```python
cadena = " Hola Ernesto "
cadena = cadena.strip("s tHo")

# Paso 1: El parámetro verifica si existe una 's' al inicio o final. Como no existe, pasa al siguiente elemento que es un espacio en blanco.

# Paso 2: Al verificar si existen espacios en blanco al inicio o final, el parámetro se encuentra con que si existen y por lo tanto los elimina. Ahora la nueva cadena es: "Hola Ernesto"

# Paso 3: El siguiente paso lógico seria verificar si existe la letra 't', sin embargo, el parámetro regresa al inicio verificando si existe la letra 's' y, al no existir, continua con el espacio en blanco.

# Paso 4: Al no existir espacios en blanco, verifica ahora con la 't' y, como tampoco existen al inicio o final, pasa a la letra 'H' mayúscula. 

# Paso 5: Al verificar si existe la letra 'H', el parámetro encuentra la letra al inicio, por lo que la elimina quedando: "ola Ernesto"

# Paso 6, 7, 8, 9 y 10: El parámetro vuelve nuevamente al inicio, recorriendo las letras 's', el espacio en blanco, la letra 't', la letra 'H' y finalmente la letra 'o'

# Paso 11: Elimina las dos 'o' al inicio o final, quedando: "la Ernest".

# Pasos siguientes: El parámetro vuelve al inicio y continua con este ciclo hasta que queda la cadena: "la Erne". Ahora, cuando llega nuevamente a la letra 'o' y comprueba que no existe al inicio o final, termina el proceso, pasando a la siguiente línea de código:

print(cadena)

# Salida: la Erne
```

El parámetro también es capaz de eliminar tabulaciones y saltos de línea:

```python
cadena = "\tHola Ernesto\n"
# \t : es para generar tabulaciones
# \n : es para generar saltos de línea
print(cadena)

# Salida:         Hola Ernesto
#
#    >>>

# Para ilustrar el salto de línea, escribimos '>>>' que seria el lugar donde se imprimiría el siguiente texto. Además, los espacios en blanco después de la palabra 'Salida:' representan la tabulación que se genera.

cadena = cadena.strip()
print(cadena)

# Salida: Hola Erenesto
# Se elimina la tabulación al inicio y el salto de linea que se genera.
```

Es importante tener en cuenta que un salto de línea o tabulación no es lo mismo que un espacio en blanco, por lo que estos no se eliminaran si añadimos caracteres dentro del parámetro:

```python

# Ejemplo 1 [Imprimimos la cadena original y despúes eliminamos tabulaciones y saltos de línea con strip()]:
cadena = "\tHola Ernesto\n"
print(cadena)
cadena = cadena.strip()
print(cadena)

# Salida:         Hola Ernesto
#
#        Hola Ernesto

#__________________________________________________________________________________

# Ejemplo 2 [Imprimimos la cadena original y despues agregamos algunos argumentos dentro del parametro strip()]:

cadena = "\tHola Ernesto\n"
print(cadena)
cadena = cadena.strip("s tHo")
print(cadena)

# Salida:         Hola Ernesto
#
#                 Hola Ernesto
#
#    >>>

#__________________________________________________________________________________

# Ejemplo 3 [Imprimimos la cadena original y despues eliminamos solo la tabulación con strip()]:

cadena = "\tHola Ernesto\n"
print(cadena)
cadena = cadena.strip("\t")
print(cadena)

# Salida:         Hola Ernesto
#
#         Hola Ernesto
#
#    >>>

#__________________________________________________________________________________

# Ejemplo 4 [Imprimimos la cadena original y despues eliminamos solo el salto de línea con strip()]:

cadena = "\tHola Ernesto\n"
print(cadena)
cadena = cadena.strip("\n")
print(cadena)

# Salida:         Hola Ernesto
#
#                 Hola Ernesto

#__________________________________________________________________________________

# Ejemplo 5 [Imprimimos la cadena original y despues eliminamos la tabulación, el salto de línea y algunos caracteres más con strip()]:

cadena = "\tHola Ernesto\n"
print(cadena)
cadena = cadena.strip("\n\ts tHo")
print(cadena)

# Salida:         Hola Ernesto
#
#         la Erne
```

> Para comprender mejor este tema, se recomienda replicar los ejercicios anteriores en la computadora y probar con diferentes combinaciones.