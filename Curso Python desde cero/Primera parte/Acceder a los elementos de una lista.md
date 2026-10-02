# Listas

En Python, cuando trabajamos con listas, surge la necesidad de acceder a los elementos contenidos dentro de la misma, ya que de esta manera podemos consultar e incluso modificar su contenido.

Para acceder a los elementos de una lista, es necesario apoyarnos de los índices, los cuales, le indicaran a nuestro programa la posición exacta del elemento con el cual deseamos trabajar dentro de la lista.

 Ejemplo: 

```python
marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
```

Al ejecutar la línea anterior, Python almacena la lista en un espacio en memoria, donde cada elemento contiene una posición:

![45_posicion_de_los_elementos_en_una_lista](../Imagenes/45_posicion_de_los_elementos_en_una_lista.png)

___

Para conocer la longitud de nuestra lista, nos podemos apoyar de la función [len()](Primera%20parte/La%20función%20len().md):

```python
marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(len(marcas))

# Salida: 4
```

Al ejecutar la línea anterior, len() nos devuelve la longitud de nuestra lista (nuestra cantidad de elementos). Y, partiendo de aquí, podemos conocer cuantas posiciones tenemos.

![45_longitud_de_una_lista_con_ayuda_de_len](../Imagenes/45_longitud_de_una_lista_con_ayuda_de_len.png)

## Acceder a los elementos de una lista

### Accediendo a un solo elemento.

Cuando ejecutamos **print(lista)**, Python nos muestra todos los elementos dentro de la lista:

```python
marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas)

# Salida: ['Apple', 'Samsung', 'Xiaomi', 'Huawei']
```

___

Para acceder a un elemento de la lista debemos escribir el nombre de nuestra lista seguido de la posición del elemento dentro de dos corchetes:

```python
# Ejemplo 1:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[1])

# Salida: Samsung
```

Ejemplo grafico:

![45_accediendo_a_los_elementos_de_una_lista](../Imagenes/45_accediendo_a_los_elementos_de_una_lista.png)

Ejemplo 2:

```python
# Ejemplo 2:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[3])

# Salida: Huawei
```

![45_accediendo_a_los_elementos_de_una_lista_v2](../Imagenes/45_accediendo_a_los_elementos_de_una_lista_v2.png)

___

Otra ventaja de las listas es que podemos trabajar con índices negativos:

```python
# Ejemplo 1:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[-1])

# Salida: Huawei
```

![45_accediendo_a_los_elementos_de_una_lista_con_indices_negativos](../Imagenes/45_accediendo_a_los_elementos_de_una_lista_con_indices_negativos.png)

Ejemplo 2:

```python
# Ejemplo 2:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[-3])

# Salida: Samsung
```

![45_accediendo_a_los_elementos_de_una_lista_con_indices_negativos_v2](../Imagenes/45_accediendo_a_los_elementos_de_una_lista_con_indices_negativos_v2.png)

### Accediendo a dos o más elementos.

Al igual que cuando tocamos el tema de [slicing](Primera%20parte/Substrings.md), podemos crear un rango dentro de la lista para obtener más de un elemento:

```python
# Ejemplo 1:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[1:3])

# Salida: ['Samsung', 'Xiaomi']
```

Donde, como se observa, Python genera un rango de donde obtendrá los valores:

![45_accediendo_a_mas_de_un_elemento_de_una_lista](../Imagenes/45_accediendo_a_mas_de_un_elemento_de_una_lista.png)

Al igual que con los substrings, podemos no especificar los índices dentro de los corchetes:

```python
# Ejemplo 2:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[:2])

# Salida: ['Apple', 'Samsung']
```

![45_accediendo_a_mas_de_un_elemento_de_una_lista_v2](../Imagenes/45_accediendo_a_mas_de_un_elemento_de_una_lista_v2.png)

Ejemplo 3:

```python
# Ejemplo 3:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[1:])

# Salida: ['Samsung', 'Xiaomi', 'Huawei']
```

![45_accediendo_a_mas_de_un_elemento_de_una_lista_v3](../Imagenes/45_accediendo_a_mas_de_un_elemento_de_una_lista_v3.png)

Ejemplo 4:

```python
# Ejemplo 4:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[:])

# Salida: ['Apple', 'Samsung', 'Xiaomi', 'Huawei']
```

![45_accediendo_a_mas_de_un_elemento_de_una_lista_v4](../Imagenes/45_accediendo_a_mas_de_un_elemento_de_una_lista_v4.png)

### Error de índice en la listas:

Cuando le indicamos a Python que busque elementos por su índice y estos no existen dentro de la lista, Python nos devolverá un error de índice:

```python
# Ejemplo 1:

marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"]
print(marcas[4])

# Salida: IndexError: list index out of range
```

![45_error_de_indice_fuera_de_rango](../Imagenes/45_error_de_indice_fuera_de_rango.png)

> Se recomienda practicar este tema modificando los ejercicios anteriores y empezando crear sus propios programas con todo lo visto hasta el momento.