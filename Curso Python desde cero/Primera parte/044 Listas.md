# Estructura de datos

En programación, las estructuras de datos son aquellas que nos permiten organizar la información de manera eficiente, y así, diseñar alternativas de solución para un determinado problema.

En Python, una de las estructuras de datos más sencilla que existe son las listas.

## Listas 

Las listas se utilizan para almacenar conjuntos de información, de esta manera, crear una colección de elementos ordenados, y a su vez, estos elementos pueden o no estar relacionados entre sí, es decir, una lista puede ser homogénea o heterogénea.

\>> Cuando hablamos de **listas homogéneas:**
Nos referimos a que todos los elementos que conforman a la lista, son del mismo tipo de dato.

\>> Cuando hablamos de **listas heterogéneas:** 
Nos referimos a que todos lo elementos que conforman a la lista, son de diferentes tipos de dato.

Además, las listas tienen la característica de ser mutables, es decir, que su contenido se puede modificar después de haber sido creadas.

## Sintaxis

La sintaxis para utilizar las listas es la siguiente:

```python
lista = [] # Donde, si la lista no contiene ningún elemento dentro de los corchetes, se considera una lista vacía.

lista_homogenea = ["Javier", "Carlos", "María"] # Todos los elementos en su interior deben ser del mismo tipo de dato

lista_heterogenea = ["nombre", 2, 3.14, True] # Los elementos en su interior son de diferente tipo de dato.
```

> A continuación, se presenta un pequeño programa para su estudio y practica con el mismo. Se recomienda realizar el mismo ejercicio en su computadora modificando las variables y las listas.

```python
print ("Lista vacia")

lista_vacia = []
print (lista_vacia)

print ("\nListas homogeneas")

vocales = ["a", "e", "i", "o", "u"]
print (vocales)

numeros_enteros = [1, 2, 3, 4, 5]
print (numeros_enteros)

numeros_decimales = [1.5, 2.2, 3.3, 4.9, 5.1]
print (numeros_decimales)

valores_booleanos = [True, False, False, True]
print (valores_booleanos)

print ("\nListas heterogenea")

datos = ['Carlos', 20, 1.70, True]
print (datos)

# Salida:

# Lista vacia
# []

# Listas homogeneas
# ['a', 'e', 'i', 'o', 'u']
# [1, 2, 3, 4, 5]
# [1.5, 2.2, 3.3, 4.9, 5.1]
# [True, False, False, True]
# 
# Listas heterogenea
# ['Carlos', 20, 1.7, True]
```