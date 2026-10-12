# Concatenación de tuplas

La concatenación de tuplas se refiere a la acción de combinar o unir dos o más tuplas para crear una nueva tupla que contenga todos los elementos de las tuplas originales en el orden que se especifican.

Como lo hemos aprendido previamente, las tuplas son estructuras de datos inmutables, lo que significa que una vez que se crean, no se pueden modificar.

Sin embargo, la concatenación de tuplas no modifica las tuplas originales, sino que crea una nueva tupla que contiene los elementos de las tuplas originales.

## Usando el operador +

```python
# Ejemplo 1:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_concatenada = tupla1 + tupla2
tupla_concatenada2 = tupla2 + tupla1

print(tupla_concatenada)
print(tupla_concatenada2)

# Salida: 

# (1, 2, 3, 4, 5, 6)
# (4, 5, 6, 1, 2, 3)
```

Usando este método podemos concatenar las tuplas que deseemos. Solo es necesario agregarlas después de cada signo de '+'. También es importante mencionar que el orden de los elementos corresponde al orden en que se concatenan las tuplas.

## Usando el operador +=

```python
# Ejemplo 2:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla1 += tupla2

print(tupla1)    # Salida: (1, 2, 3, 4, 5, 6)
```

Al utilizar el operador '+=', Python crea una nueva tupla con el mismo nombre. Por lo tanto, aunque parezca que se ha modificado la tupla original, en realidad ha sido reemplazada.

# Usando la función tuple()

```python
# Ejemplo 3:

tupla1 = (1, 2, 3)
lista = [4,5,6]

tupla_concatenada = tupla1 + tuple(lista)

print(tupla_concatenada)    # Salida: (1, 2, 3, 4, 5, 6)
```

Es importante mencionar que no se puede concatenar una tupla con una lista. Para ello, es necesario utilizar la función [tuple()](Primera%20parte/090%20La%20función%20tuple().md) para convertir la lista antes de concatenarla.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.

