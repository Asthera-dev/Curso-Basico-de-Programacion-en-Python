# Desempaquetado de tuplas con for

Al igual que cuando utilizamos dos variables para poder utilizar el método [item()](Primera%20parte/080%20Diccionarios%20y%20el%20ciclo%20for%20(C%C3%B3mo%20recorrer%20un%20diccionario).md#Ejemplo%20de%20Sintaxis%202) con el ciclo for, este caso es muy similar:

Ejemplo:

```python
tupla = (("001", "Manzana", "rojo"),
		("002", "Pera", "verde"))

for codigo, fruta, color in tupla:
	print(f"La {fruta} tiene el código {codigo} y es de color {color}")

# Salida:

# La Manzana tiene el código 001 y es de color rojo
# La Pera tiene el código 002 y es de color verde
```

Al recorrer nuestra tupla, el ciclo for encuentra tuplas en su interior que contienen tres elementos. Podemos desempaquetar estas tuplas mientras utilizamos el ciclo, colocando un número igual de variables que de elementos dentro de estas tuplas.

Si colocamos un número mayor o menor de variables, Python nos marcará un error.

> Se recomienda practicar este tema creando sus propias tuplas y programas. Esto con el objetivo de lograr una compresión más profunda del tema.

