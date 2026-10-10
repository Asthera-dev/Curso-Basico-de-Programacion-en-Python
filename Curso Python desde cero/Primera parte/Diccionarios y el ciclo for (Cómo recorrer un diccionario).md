# Recorriendo un diccionario

En Python, para recorrer un diccionario de manera automatizada, lo ideal es utilizar el ciclo for.

En esta nota se mostrarán dos alternativas de sintaxis con lo cual se podrá realizar este recorrido.

## Ejemplo de Sintaxis 1:

```python
# Ejemplo 1:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

for key in dict_name:
	print(f"{key} : {dict_name[key]}")

# Salida:

# a : 1
# b : 2
# c : 3
```

Como se observa en el ejemplo anterior, al recorrer un diccionario con el ciclo [for](Primera%20parte/El%20ciclo%20o%20bucle%20for.md), este ciclo toma las claves dentro del diccionario una a una y las almacena temporalmente en la variable asignada (en este caso 'key'). Después, con el método aprendido en la nota: '[Acceder a los elementos de un diccionario](Primera%20parte/Acceder%20a%20los%20elementos%20de%20un%20diccionario.md)', podemos acceder al valor de dicha clave.

## Ejemplo de Sintaxis 2:

```python
# Ejemplo 2:

dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

for key, value in dict_name.items():
	print(f"{key} : {value}")

# Salida:

# a : 1
# b : 2
# c : 3
```

Como se observa en el ejemplo 2, con ayuda de '[El método items()](Primera%20parte/El%20método%20items().md)', podemos extraer tanto la clave como el valor almacenado. Para esto es necesario especificar dos variables donde:

\>> La primera variable será la que almacenará la clave (en este caso **'key'**).
\>> La segunda variable será la que almacenará el valor (en este caso **'value'**)

Finalmente:

> Se anima al lector a modificar el método items() del ejercicio 2 por otros métodos como: '[El método keys()](Primera%20parte/El%20método%20keys().md)' y '[EL método values()](Primera%20parte/EL%20método%20values().md)'. Donde, a diferencia del método items(), estos métodos necesitan solo una variable:

```python
dict_name = {"a": 1,
			 "b": 2,
			 "c": 3
			 }

print(f"Método '.keys()':")

for key in dict_name.keys():
	print(f"{key}")

print(f"\nMétodo '.values()':")

for key in dict_name.values():
	print(f"{key}")
```