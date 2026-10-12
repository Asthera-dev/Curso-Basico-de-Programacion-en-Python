# Los métodos istitle() y title()

En Python, es posible convertir la primera letra de cada palabra de un String en mayúsculas, y a su vez, convertir el resto de letras que componen a cada palabra de un String en minúsculas.

Para realizar esta acción, contamos con los métodos istitle() y title(), los cuales se utilizan para identificar si la primera letra de cada palabra comienza con mayúscula, y el resto de letras se encuentran en minúsculas, y de no ser así, realizar la respectiva conversión.

La sintaxis para los métodos istitle() y title() es la siguiente:

```python
nombre_variable.istitle()
nombre_variable.title()
```

Supongamos que solicitamos al usuario de nuestro programa que introduzca su nombre:

```python
# Al momento de diseñar programas debemos anticiparnos a las variaciones en las entradas que pueda brindar el usuario, como:

# Un nombre mal escrito alternando mayúsculas y minúsculas:
nombre_completo = "carLOS galLaRDo"

# Al aplicar el método istitle(), python nos devolvera un booleano:
print(nombre_completo.istitle())   # Salida: False

#__________________________________________________________________________________

# Lo que hace istitle() para decidir es: Verificar que la PRIMERA LETRA de cada palabra este en mayúscula y el resto en minúsculas.

# Por lo tanto:

print("Hola mundo".istitle())   # Devolvera False
print("Hola Mundo".istitle())   # Devolvera True
print("Hola MuNdo".istitle())   # Devolvera False

#__________________________________________________________________________________

# Ahora, con title(), podemos convertir nuestra cadena de texto a una donde la primera letra de cada palabra siempre es mayuscula y el resto minusculas:

print("carLOS galLaRDo".title())   # Salida: Carlos Gallardo
```

> Para comprender mejor este tema, se recomienda realizar el siguiente ejercicio en su computadora modificando las variables y/o las líneas de código:

```python
first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f'{first_name} {last_name}'

print(f"\n¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el método title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")

full_name = full_name.title()
print(f"\n¿El formato del método title() se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado el método title() de manera permante: {full_name}")

# Salida [Primero solicitando los datos]:

# Nombre: isai
# Apellido: montiel
#
# ¿El formato del metodo title() se ha aplicado?: False
# Aplicando el método title(): Isai Montiel
# Volvemos a imprimir el nombre: isai montiel
#
# ¿El formato del método title() se ha aplicado?: True
# Se ha aplicado el método title() de manera permante: Isai Montiel
```
