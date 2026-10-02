# Ciclo o bucle for

En Python, el ciclo o bucle for es una estructura de control que nos permite repetir un bloque de instrucciones (sentencias), cierta cantidad de veces.

## Sintaxis

Sintaxis del ciclo o bucle for

```python
for variable in objeto_iterable:
    Instrucción...
    Instrucción...
    Instrucción...
```

## Objeto iterable

Un objeto iterable es aquel que permite recorrer sus elementos uno a uno. Como por ejemplo, una cadena de caracteres.

Como por ejemplo: **"Hola me llamo Isai"**

En este caso, esta cadena de caracteres es un objeto iterable porque, con ayuda de un índice, podemos recorrer uno a uno sus elementos. 

Ejemplo:

```python
string = "Hola"

for character in string:
	print(character)
print("Fin del programa")

# Salida: 

# H
# o
# l
# a
# Fin del programa
```

Donde:
* **String**: Es nuestro objeto iterable ya que podemos recorrer uno a uno sus elementos con ayuda de un índice.
* **in**: Es la palabra reservada que acompaña al ciclo for y siempre debe ir después de nuestra variable (en este caso "character") y antes de nuestro objeto iterable (en este caso "string"). Este le indica al ciclo que trabajara dentro de un objeto iterable.
* **character**: Es la variable que almacenara temporalmente los elementos que el ciclo for vaya recorriendo. Esta variable puede llamarse como el usuario guste y solo servirá dentro del ciclo for (en este ejemplo, la variable se llama **character**.
* **:** Los dos puntos al final ' : ', al igual que con el bucle [while](Primera%20parte/Bucle%20o%20ciclo%20while.md), indican al ciclo que se prepare para leer las instrucciones dentro del mismo.

La ejecución paso a paso del ejemplo anterior es:
```python
string = "Hola"

for character in string:
	print(character)

print("Fin del programa")

# Iteración 1:
#	El índice se coloca en el primer elemento del objeto iterable; 'H', y la variable 'character' toma este valor.
#   Posteriormente, se ejecuta la instrucción: print(character).
#   Como ya no existen mas instrucciones que ejecutar dentro del bucle, este recorre el siguiente elemento.

# Iteración 2:
#	El índice se coloca en el segundo elemento del objeto iterable; 'o', y la variable 'character' toma este valor.
#   Posteriormente, se ejecuta la instrucción: print(character).
#   Como ya no existen mas instrucciones que ejecutar dentro del bucle, este recorre el siguiente elemento.

# Iteración 3:
#	El índice se coloca en el tercer elemento del objeto iterable; 'l', y la variable 'character' toma este valor.
#   Posteriormente, se ejecuta la instrucción: print(character).
#   Como ya no existen mas instrucciones que ejecutar dentro del bucle, este recorre el siguiente elemento.

# Iteración 4:
#	El índice se coloca en el cuarto elemento del objeto iterable; 'o', y la variable 'character' toma este valor.
#   Posteriormente, se ejecuta la instrucción: print(character).
#   Como ya no existen mas instrucciones que ejecutar dentro del bucle, este recorre el siguiente elemento.

# Como ya no existe ningún elemento por recorrer, el bucle for termina y pasa a la siguiente instrucción fuera del bucle que es: print("Fin del programa"). Dándonos así la siguiente salida:

# H
# o
# l
# a
# Fin del programa
```

> De momento lo dejaremos hasta aquí, pero en la siguiente nota continuaremos trabajando y practicando con el "ciclo o buble for".