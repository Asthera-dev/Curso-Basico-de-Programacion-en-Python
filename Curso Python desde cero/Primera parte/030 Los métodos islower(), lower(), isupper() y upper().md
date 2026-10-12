# Métodos de formato

En Python, contamos con métodos que nos permiten convertir todas las letras de una cadena de caracteres a mayúsculas, o bien, a minúsculas.

Y a su vez, también contamos con métodos para identificar si una cadena de caracteres se encuentra completamente en mayúsculas o en minúsculas.

## Métodos islower() y lower()

Se utilizan para identificar si todas las letras de una cadena de caracteres se encuentran en minúsculas, y de no ser así, convertir todas las letras en minúsculas.

La sintaxis de los métodos islower() y lower() es la siguiente:

```python
nombre_variable.islower() # El metodo en minúsculas, sin espacios y con dos
nombre_variable.lower()   # parentesis sin nada en su interior.
```

Supongamos que solicitamos al usuario que introduzca una palabra:

```python
nombre_variable = "PYTHON Desde Cero"

# Al aplicar el método islower() python nos devuelve un booleano
print(nombre_variable.islower())   # Salida: False

#__________________________________________________________________________________

# Lo que hace islower() para decidir es: Verificar que TODAS LAS LETRAS una cadena de texto este en MINÚSCULAS.

# Por lo tanto:

print("Hola mundo".islower())   # Devolvera False
print("hola mundo".islower())   # Devolvera True
print("hola muNdo".islower())   # Devolvera False

#__________________________________________________________________________________

# Ahora, con lower(), podemos convertir nuestra cadena de texto a una donde todas las letras que la componen estén en minúsculas:

print("PYTHON Desde Cero".lower())   # Salida: python desde cero
``` 

## Métodos isupper() y upper()

Se utilizan para identificar si todas las letras de una cadena de caracteres se encuentran en mayúsculas, y de no ser así, convertir todas las letras en mayúsculas.

La sintaxis de los métodos isupper() y upper() es la siguiente:

```python
nombre_variable.isupper() # El metodo en minúsculas, sin espacios y con dos
nombre_variable.upper()  # parentesis sin nada en su interior.
```

Para visualizar estos métodos, utilicemos el mismo ejemplo:

```python
nombre_variable = "PYTHON Desde Cero"

# Al aplicar el método isupper() python nos devuelve un booleano
print(nombre_variable.isupper())   # Salida: False

#__________________________________________________________________________________

# Lo que hace islower() para decidir es: Verificar que TODAS LAS LETRAS una cadena de texto este en MAYÚSCULAS.

# Por lo tanto:

print("Hola mundo".isupper())   # Devolvera False
print("HOLA MUNDO".isupper())   # Devolvera True
print("HOLA MUNDo".isupper())   # Devolvera False

#__________________________________________________________________________________

# Ahora, con upper(), podemos convertir nuestra cadena de texto a una donde todas las letras que la componen estén en mayúsculas:

print("PYTHON Desde Cero".upper())   # Salida: PYTHON DESDE CERO
``` 

Algo importante a mencionar es que ambos métodos pueden trabajar sin problema aun si en su interior contienen números o caracteres especiales:

```python
cadena = "*!Yo nací en los - años - 90 en la calle 32¡*"
print(cadena.lower())
print(cadena.upper())

# Salida: *!yo nací en los - años - 90 en la calle 32¡*
#         *!YO NACÍ EN LOS - AÑOS - 90 EN LA CALLE 32¡*

# O tambien:

minusculas = "*!yo nací en los - años - 90 en la calle 32¡*"
mayusculas = "!YO NACÍ EN LOS - AÑOS - 90 EN LA CALLE 32¡"
print(minusculas.islower())
print(mayusculas.isupper())

# Salida: True
#         True
```

> Para comprender mejor este tema, se recomienda realizar el siguiente ejercicio en su computadora modificando las variables y/o las líneas de código:

```python
string = input("Introduce un String: ")

print(f"\nTodas las letras están en minúsculas?: {string.islower()}")
string = string.lower()
print(f"String en minúsculas: {string}")

print(f"\n¿Todas las letras están en mayúsculas?: {string.isupper()}")
print(f"String en mayúsculas: {string.upper()}")
print(f"String original: {string}")

# Salida [Primero solicitando los datos]:

# Introduce un String: PYTHON Desde Cero
#
# Todas las letras están en minúsculas?: False
# String en minúsculas: python desde cero
#
# ¿Todas las letras están en mayúsculas?: False
# String en mayúsculas: PYTHON DESDE CERO
# String original: python desde cero
```