# Diccionarios

En Python, un diccionario es una estructura de datos que se utiliza para almacenar un conjunto de elementos no ordenados, y al igual que las lista, un diccionario puede ser homogéneo o heterogéneo.

Es decir, todos los elementos que conforman a un diccionario pueden ser del mismo tipo de dato, o bien, de diferentes tipos de datos.

Además, los diccionarios al igual que las listas, tienen la característica de ser mutables, esto quiere decir, que después de haber sido creados su contenido se puede modificar.

## Sintaxis

La sintaxis para crear un diccionario, es la siguiente:

```python
nombre_diccionario = {} # Diccionario vacío
nombre_diccionario = {key: elemento} # Diccionario con un elemento
nombre_diccionario = {key: elemento, key: elemento, ...} # Diccionario con dos elementos o más
```

Donde:
* **key**: Es la clave para hacer referencia a un elemento dentro del diccionario. Puede ser de tipo entero o de tipo String
* **elemento**: Es el elemento que queremos almacenar.

Ahora que ya sabemos la sintaxis para crear un diccionario, veamos su implementación:

```python
nombre_diccionario = {"a": 1, "b": 2, "c": 3} # Diccionario homogeneo (todos sus elementos son del mismo tipo de dato)

nombre_diccionario = {1: "hola", 2: [0, 1, 2]} # Diccionario heterogeneo (sus elementos corresponden a diferente tipo de dato)

nombre_diccionario = {"a": {"a": 1}, 1: [0, 1, 2]} # Diccionario heterogeneo con claves mixtas (diferente tipo de dato). La llave "a", aunque se llame igual, hace referencia a un tipo diferente de elemento.
```

Como se observa en el ejemplo anterior, las llaves (keys) pueden ser tanto Strings como valores numéricos y se pueden combinar. Sin embargo, por comodidad a la hora de programar, se recomienda que las llaves sean de un mismo tipo de dato.

Además, nuestro elemento puede ser de cualquier tipo: String, Entero, Flotante, Lista, Diccionario, etc.

Ahora:

```python
nombre_diccionario = {"a": 1, "b": 1, "a": 3}
```

Como se observa en la línea de código anterior, existen dos claves iguales: 'a'.
Esto es incorrecto porque los diccionarios solo admiten claves únicas y, cuando esto sucede, Python toma la ultima aparición de la llave repetida y elimina el resto. Por lo tanto, nuestro diccionario final seria:

```python
nombre_diccionario = {"a": 1, "b": 1}
```

Finalmente:

 > Se recomienda practicar este tema modificando los parámetros y valores de los ejercicios anteriormente presentados para comprender su funcionamiento.
 
