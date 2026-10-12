# Elementos por segmentación

Para acceder a los elementos de una tupla, además de los índices, también contamos con el operador de segmentación. 

El operador de segmentación en Python, se utiliza para obtener una subsecuencia de elementos de una lista, una tupla o un String.

## Sintaxis

La sintaxis para utilizar el operador de segmentación es la siguiente.

```python
# Para trabajar con este método podemos trabajar con un mínimo de dos elementos y un máximo de tres:

nombre_tupla[inicio : final] # Trabajando con dos elementos 

nombre_tupla[inicio : final : saltos] # Trebajando con tres elementos
```

Como se observa, la sintaxis es muy similar al [slicing](036%20Substrings.md) y a la forma de [acceder a los elementos de una lista](045%20Acceder%20a%20los%20elementos%20de%20una%20lista.md).

Los valores asignados a el inicio, final y saltos, deberán ser valores enteros, y a su vez, el valor que se le asigne a los índices pueden ser positivos o negativos.

Ejemplo:

```python
# Ejemplo 1:

tupla_vocales = ("a", "e", "i", "o", "u")

print(tupla_vocales[0:2])    # Salida: ('a', 'e')
print(tupla_vocales[::2])    # Salida: ('a', 'i', 'u')
print(tupla_vocales[-3:])    # Salida: ('i', 'o', 'u')
```

Como se observa, al trabajar con este método Python nos devuelve una tupla más "pequeña". Esto debido a que estamos segmentando la tupla original.

Finalmente:

> Se recomienda practicar este tema creando sus propias tuplas y programas. Esto con el objetivo de lograr una compresión más profunda del tema.

