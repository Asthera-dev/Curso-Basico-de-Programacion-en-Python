# El método copy()

El método copy() se utiliza para crear una copia de un objeto en Python, como pueden ser las listas, matrices o diccionarios.

Este método es muy útil ya que de esta manera podemos realizar modificaciones al objeto que hemos copiado, sin afectar el objeto original y viceversa.

## Sintaxis

La sintaxis para utilizar el método copy(), es la siguiente:

```python
nombre_objeto.copy()
```

Ejemplo:

```python
diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

diccionario_copia = diccionario.copy()

print(diccionario_copia)    # Salida: {'a': 1, 'b': 2, 'c': 3}
```

Como se observa, es necesario almacenar nuestra copia en otra variable para posteriormente poder trabajar sobre ella.

Finalmente:

> Se recomienda ejecutar el programa a continuación para observar su salida. Además, también se anima al lector a modificar los valores y agregar más elementos para crear un programa más completo.

```python
diccionario = {"nombre": "Diego",
			   "apellido": "Lozano",
			   "edad": 25
			   }

print(f"Diccionario original: {diccionario}")

diccionario_copia = diccionario.copy()
print(f"Diccionario copia: {diccionario_copia}")
```