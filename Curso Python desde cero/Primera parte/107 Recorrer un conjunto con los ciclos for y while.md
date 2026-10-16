# Recorriendo un conjunto con el ciclo for y while

Recordemos que un conjunto es un elemento al cual no podemos acceder a sus elementos mediante índices. Es por esta razón que es recomendable utilizar el ciclo for:

```python
nums = {1, 2, 3, 4, 5}

# Recorrer conjunto utilizando for
print("Recorriendo conuunto con el ciclo for")
for elemento in nums:
	print(elemento)


# Recorrer conjunto con el ciclo while
print(f"\n\nRecorriendo conjuntos con el cilo while")
conjunto_lista = list(nums) # Convertimos el conjunto a una lista para poder recorrer sus elementos.

indice = 0
while indice < len(conjunto_lista):
	print(conjunto_lista[indice])
	indice +=1

# Salida:

# Recorriendo conuunto con el ciclo for
# 1
# 2
# 3
# 4
# 5
# 
# 
# Recorriendo conjuntos con el cilo while
# 1
# 2
# 3
# 4
# 5
```

Como se observa, trabajar con el ciclo for es más cómodo y sencillo.

Finalmente:

> Se recomienda practicar este tema modificando el ejercicio anterior y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.