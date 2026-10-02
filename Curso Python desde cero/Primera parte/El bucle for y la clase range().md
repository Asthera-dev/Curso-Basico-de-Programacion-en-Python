# Sintaxis bucle for con range()

Lo que veremos en esta nota será aprender el comportamiento del ciclo for en conjunto con la clase range() 

Para empezar, es necesario tener en mente la sintaxis del [ciclo o bucle for](El%20ciclo%20o%20bucle%20for.md#Sintaxis):

```python
for variable in objeto_iterable:
	instrucción...
	instrucción...
	instrucción...
```

Nosotros nos centraremos en el objeto iterable. Donde podemos usar la clase range() en sus tres formas distintas:

```python
for variable in range(start, stop, step): 
	instrucción...
	instrucción...
	instrucción...
```

> Para comprender mejor lo anterior, veamos la ejecución de un pequeño código:

```python
for indice in range(1,5):
	print(indice)

print("Fin del programa.")

# Salida:

# 1
# 2
# 3
# 4
# Fin del programa.
```

Donde el programa ejecuta los siguientes pasos:

\>> Python, al detectar la palabra reservada **for**, se prepara para entrar en un ciclo. 

\>> Después, crea una variable temporal con el nombre asignado (en este caso 'indice')

\>> Posteriormente, con la palabra reservada **in**, Python se prepara para recorrer el objeto iterable con un índice elemento a elemento (en este caso usando **range(1,5)**).

\>> **range(1, 5)** crea un intervalo de números del 1 al 4 con un salto de uno que posteriormente for recorre.

\>> En cada ciclo, for ejecuta las líneas de código en su interior (En este caso **'print(indice)'**). Obteniendo de esta forma las impresiones de los números del 1 al 4.

\>> Cuando for no puede recorrer más elementos del objeto iterable (porque ya no hay más que recorrer), se termina el ciclo. Y se ejecuta la siguiente línea de código fuera del bucle (en este caso "Fin del programa.").

> Se recomienda realizar diferentes ejercicios modificando los diferentes parámetros de range() para comprender su funcionamiento.