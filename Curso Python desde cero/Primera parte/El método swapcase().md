# El método swapcase()

En Python, contamos con el método swapcase(), que a diferencia de los métodos [lower() y upper()](Primera%20parte/Los%20métodos%20islower(),%20lower(),%20isupper()%20y%20upper().md), nos permite invertir todas las letras de una cadena de caracteres, donde las mayúsculas se convierten en minúsculas y las minúsculas se convierten en mayúsculas.

La sintaxis para utilizar este método es la siguiente:

```python
nombre_variable.swapcase() # El metodo en minúsculas, sin espacios y con dos parentesis vacios.
```

Supongamos que tenemos una cadena de caracteres con mayúsculas y minúsculas:

```python
nombre_variable = "Hola Mundo"
print(nombre_variable.swapcase())   # Salida: hOLA mUNDO
```

> Para comprender mejor este tema, se recomienda realizar el siguiente ejercicio en su computadora modificando las variables y/o las líneas de código:

```python
txt_lower_upper = "PYTHON Desde Cero"
print(txt_lower_upper.swapcase())

txt_upper = "CADENA DE MAYUSCULAS"
print(txt_upper.swapcase())

txt_lower = "cadena de minusculas"
print(txt_lower.swapcase())

txt_number = "1234!-*"
print(txt_number)

print() # Solo agrega un salto de línea
print(txt_lower_upper)
print(txt_upper)
print(txt_lower)
print(txt_number)

# Salida: python dESDE cERO
#         cadena de mayusculas
#         CADENA DE MINUSCULAS
#         1234!-*
#
#         PYTHON Desde Cero
#         CADENA DE MAYUSCULAS
#         cadena de minusculas
#         1234!-*
```