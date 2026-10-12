# El método clear()

Este método se utiliza para eliminar todos los elementos de un objeto en Python. Este objeto puede ser una lista, un diccionario o un conjunto.

## Sintaxis

La sintaxis para utilizar el método clear(), es la siguiente:

```python
nombre_objeto.clear()
```

El objeto, como se mencionó, puede ser una **lista**, **conjunto** o **diccionario**.

Ejemplo:

```python
# Ejemplo 1:

diccionario = {"a": 1,
			   "b": 2,
			   "c": 3
			   }

diccionario.clear() 
print(diccionario)    # Salida: {}
```

Como se observa, al aplicar este método, Python elimina el contenido del diccionario y nos deja con un diccionario vacío.

```python
# Ejemplo 2:

empleados = {"Juan": {"edad": 28, "salario": 25000},
			 "Maria": {"edad": 24, "salario": 20000}
			}

print(f"Diccionario original: {empleados}")

empleados.clear()

print(f"Diccionario actualizado: {diccionario}")

# Salida:

# Diccionario original: {'Juan': {'edad': 28, 'salario': 25000}, 'Maria': {'edad': 24, 'salario': 20000}}
# Diccionario actualizado: {}
```
