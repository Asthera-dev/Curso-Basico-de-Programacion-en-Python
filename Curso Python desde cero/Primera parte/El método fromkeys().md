# El método fromkeys()

El método fromkeys() es una función incorporada de Python que se utiliza para crear un nuevo diccionario con claves de una secuencia dada y valores previamente establecidos.

Es decir, el método **fromkeys()** se encarga de tomar una secuencia de claves y un valor predeterminado, y crear un nuevo diccionario con esas claves y el mismo valor para todas ellas.

Este método es útil porque permite crear diccionarios con claves predefinidas y valores predeterminados sin la necesidad de escribir mucho código.

Principalmente cuando se trabaja con grandes conjuntos de datos o cuando se necesita crear varios diccionarios con la misma estructura.

## Sintaxis
 
La sintaxis para utilizar el método fromkeys(), es la siguiente:

```python
# Este metodo trabaja con un mínimo de un argumento y un maximo de dos.

nombre_diccionario = dict.fromkeys(secuencia) # Trabajando con un argumento
nombre_diccionario = dict.fromkeys(secuencia, valor) # Trabajando con los dos argumentos
```

Donde:
* **Dict**: Es la abreviatura de "dictionary" que en español significa "diccionario". En Python, **'dict'** se refiere a una clase incorporada que se utiliza para crear objetos de tipo diccionario.
* **Secuencia**: Es la secuencia de claves.
* **valor**: Es el valor preestablecido para todas las claves de nuestra secuencia.

Ejemplos:

```python
# Ejemplo 1 (trabajando con un solo argumento):

secuencia = ["uno", "dos", "tres"]
name_dic = dict.fromkeys(secuencia)

print(name_dic)    # Salida: {'uno': None, 'dos': None, 'tres': None}
```

Como se observa, este método utiliza la 'secuencia' dada para crear las llaves del diccionario y, como no se especifico el segundo argumento, de manera predeterminada Python le agrega la palabra **'None'**, indicando que no contiene nada en su interior.

```python
# Ejemplo 2 (trabajando con ambos argumentos):

secuencia = ["uno", "dos", "tres"]
valor = 5
name_dic = dict.fromkeys(secuencia, valor)

print(name_dic)    # Salida: {'uno': 5, 'dos': 5, 'tres': 5}
```

Ahora, al agregar el segundo valor, Python remplazara la palabra 'none' por el valor asignado.

Ahora, ¿Qué sucede si utilizamos un diccionario como secuencia?:

```python
# Ejemplo 3:

secuencia = {"uno": 1, "dos": 2, "tres": 3}
valor = 5
name_dic = dict.fromkeys(secuencia, valor)

print(name_dic)    # Salida: {'uno': 5, 'dos': 5, 'tres': 5}
```

Como se observa en el ejemplo 3, Python utiliza las claves de mi diccionario para usarlas en el nuevo diccionario. Además, ignora los valores que ya tenían asignados y, en su lugar, le asigna mi valor especificado.

Veamos un ejemplo más:

```python
# Ejemplo 3:

secuencia = "hola"
valor = 1
# En lugar de la palabra 'dict' podemos usar dos llaves: {}
name_dic = {}.fromkeys(secuencia, valor) 

print(name_dic)    # Salida: {'h': 1, 'o': 1, 'l': 1, 'a': 1}
```

Como se observa, el método igualmente funciona usando dos llaves ' {} ' en lugar de la palabra 'dict'. Además, como se observa, este método itera sobre el string para crear las llaves del nuevo diccionario agregándoles el valor especificado.

Finalmente:

> Se anima al lector a utilizar este método para automatizar la creación de diccionarios con un volumen considerable de claves. Esto para mejorar la compresión del tema y, en general, del funcionamiento de los diccionarios en Python.