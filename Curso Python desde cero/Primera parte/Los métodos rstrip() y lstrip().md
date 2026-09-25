## El método rstrip()

Se utiliza para eliminar únicamente caracteres especificados al final de una cadena.

Al igual que el método [strip()](Primera%20parte/El%20método%20strip().md), si no se especifica uno o más caracteres a eliminar, solo eliminara espacios en blanco y saltos de línea.

La sintaxis para utilizar el método rstrip() es la siguiente:

```python
# Sintaxis básica:
cadena.rstrip()

#__________________________________________________________________________________

# Ejemplo 1:
cadena = " Hola Ernesto "
cadena = cadena.rstrip()
print(cadena)

# Salida: " Hola Ernesto"

#__________________________________________________________________________________

# Ejemplo 2:
cadena = " Hola Ernesto "
cadena = cadena.rstrip(" oH")
print(cadena)

# Salida: " Hola Ernest"

#__________________________________________________________________________________

# Ejemplo 3:
cadena = "\tHola Ernesto\n"
cadena = cadena.rstrip(" oH\t\n")
print(cadena)

# Salida:   	Hola Ernest
```

## El método lstrip()

Se utiliza para eliminar únicamente caracteres especificados al inicio de una cadena.

Al igual que los métodos anteriores, si no se especifica uno o más caracteres a eliminar, solo eliminara espacios en blanco y saltos de línea.

La sintaxis para utilizar el método lstrip() es la siguiente:

```python
# Sintaxis básica:
cadena.lstrip()

#__________________________________________________________________________________

# Ejemplo 1: 
cadena = " Hola Ernesto "
cadena = cadena.lstrip()
print(cadena)

# Salida: "Hola Ernesto "

#__________________________________________________________________________________

# Ejemplo 2: 
cadena = " Hola Ernesto "
cadena = cadena.lstrip(" oH")
print(cadena)

# Salida: "la Ernesto "

#__________________________________________________________________________________

# Ejemplo 3:
cadena = "\tHola Ernesto\n"
cadena = cadena.lstrip("s tHo\t\n")
print(cadena)

# Salida: la Ernesto
#
#    >>>
```

> Para comprender mejor este tema, se recomienda replicar los ejercicios anteriores en la computadora y probar con diferentes combinaciones.