# Sentencias condicionales anidadas en Python

Las sentencias condicionales anidadas, se presentan cuando por el camino de verdadero o falso de una sentencia condicional hay otra sentencia condicional.

Es decir, cuando trabajamos con sentencias condicionales simples, compuestas o múltiples, podemos colocar dentro de la instrucción o instrucciones a ejecutar de cada una de estas sentencias, otra sentencia condicional. 

En conclusión, las sentencias condicionales anidadas consisten en tener una instrucción condicional dentro de otra y, dependiendo de si la condición de la primera sentencia condicional se cumple o no se cumple, se ejecutará otra sentencia condicional. 

De esta manera, tendremos una condición dentro de otra condición, ampliando la cantidad de opciones para que nuestros programas puedan resolver un problema, sin importar la cantidad de situaciones que se presenten.

> Para consolidar las bases de esta sección, se recomienda crear el siguiente programa:

```python
# Crear un programa titulado:
'''
==========
Conversor
==========
'''

# La interfaz del programa debera contener las siguientes opciones:

'''
Menú de opciones:
Presiona 1 para convertir de número a palabra.
Presiona 2 para convertir de palabra a número.
'''

# El usuario debera poder escoger entre una de las dos opciones anteriores. En caso de ingresar otro valor, el programa deber de mostrar el mensaje: 'Opción no disponible'.

####################################################

# Cuando el usuario seleccione la opción 1:

#	1. Debera ingresar cualquier número en digitos.
#	2. Si el número ingresado es (>= 1 y <= 5):
#		* Se debera mostrar el número en letras.
#		* En caso de que el número se encuentre fuera de este rango se debera mostrar el mensaje: 'El número seleccionado no esta registrado.'


# Cuando el usuario seleccione la opción 2:

#	1. Debera ingresar cualquier número en letras.
#	2. Si el número ingresado es (>= 1 y <= 5):
#		* Se debera mostrar el número en digitos.
#		* En caso de que el número se encuentre fuera de este rango se debera mostrar el mensaje: 'El número seleccionado no esta registrado.'
```

> Mas adelante se introducirá el uso de 'lower()' y 'upper()' para evitar errores en el programa.
> Sin embargo, si lo desea, puede consultar esta nota en el siguiente archivo: [Los métodos islower(), lower(), isupper() y upper()](Los%20métodos%20islower(),%20lower(),%20isupper()%20y%20upper().md)

